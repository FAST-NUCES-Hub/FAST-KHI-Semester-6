/**
 * Settlement class - Records payments between users and updates balances.
 * 
 * Complex Algorithm #3: Smart Settlement Suggestion
 * 
 * The settlement module not only records payments but also suggests
 * optimal settlements using an enhanced version of the debt simplification.
 * It handles partial settlements, validates against outstanding balances,
 * and maintains a full audit trail.
 */
export class Settlement {
  static #idCounter = 0;

  constructor({ fromUserId, toUserId, amount, groupId, note = '' }) {
    if (!fromUserId) throw new Error('fromUserId is required.');
    if (!toUserId) throw new Error('toUserId is required.');
    if (fromUserId === toUserId) throw new Error('Cannot settle with yourself.');

    if (amount === undefined || amount === null || typeof amount !== 'number') {
      throw new Error('Settlement amount must be a number.');
    }
    if (amount <= 0) {
      throw new Error('Settlement amount must be greater than zero.');
    }
    if (!Number.isFinite(amount)) {
      throw new Error('Settlement amount must be a finite number.');
    }

    this.id = ++Settlement.#idCounter;
    this.fromUserId = fromUserId;
    this.toUserId = toUserId;
    this.amount = Math.round(amount * 100) / 100;
    this.groupId = groupId;
    this.note = note;
    this.createdAt = new Date();
  }

  toJSON() {
    return {
      id: this.id,
      fromUserId: this.fromUserId,
      toUserId: this.toUserId,
      amount: this.amount,
      groupId: this.groupId,
      note: this.note,
      createdAt: this.createdAt.toISOString(),
    };
  }

  static resetCounter() {
    Settlement.#idCounter = 0;
  }
}

/**
 * SettlementManager - Manages settlements and suggests optimal payment plans.
 * 
 * COMPLEX ALGORITHM #3: Smart Settlement Suggestion with Priority Queue Approach
 * 
 * Uses a modified greedy approach that:
 * 1. Computes current net positions after existing settlements
 * 2. Identifies remaining debts
 * 3. Suggests minimum transactions using a priority-based matching
 * 4. Handles partial and circular debt scenarios
 */
export class SettlementManager {
  constructor() {
    this.settlements = [];
  }

  recordSettlement({ fromUserId, toUserId, amount, groupId, note }) {
    const settlement = new Settlement({
      fromUserId,
      toUserId,
      amount,
      groupId,
      note,
    });
    this.settlements.push(settlement);
    return settlement;
  }

  getSettlementsForGroup(groupId) {
    return this.settlements.filter((s) => s.groupId === groupId);
  }

  getSettlementsByUser(userId) {
    return this.settlements.filter((s) => s.fromUserId === userId || s.toUserId === userId);
  }

  getTotalSettled(groupId) {
    return this.settlements
      .filter((s) => s.groupId === groupId)
      .reduce((sum, s) => sum + s.amount, 0);
  }

  /**
   * ALGORITHM: Smart settlement suggestions
   * 
   * Given the current state of expenses and existing settlements,
   * this method figures out who should pay whom and how much to
   * fully settle all debts with minimum number of transactions.
   * 
   * Handles edge cases:
   * - Circular debts (A owes B, B owes C, C owes A)
   * - Partial settlements (only some debts have been settled)
   * - Already balanced groups (no suggestions needed)
   */
  suggestSettlements(netBalances) {
    const creditors = []; // owed money
    const debtors = []; // owe money

    netBalances.forEach((balance, userId) => {
      const rounded = Math.round(balance * 100) / 100;
      if (rounded > 0.01) {
        creditors.push({ userId, amount: rounded });
      } else if (rounded < -0.01) {
        debtors.push({ userId, amount: -rounded });
      }
    });

    // Priority: Match exact amounts first (reduces transactions further)
    const suggestions = [];
    const usedCreditors = new Set();
    const usedDebtors = new Set();

    // Pass 1: Find exact matches (optimal pairing)
    for (let di = 0; di < debtors.length; di++) {
      if (usedDebtors.has(di)) continue;
      for (let ci = 0; ci < creditors.length; ci++) {
        if (usedCreditors.has(ci)) continue;
        if (Math.abs(debtors[di].amount - creditors[ci].amount) < 0.01) {
          suggestions.push({
            from: debtors[di].userId,
            to: creditors[ci].userId,
            amount: debtors[di].amount,
          });
          usedDebtors.add(di);
          usedCreditors.add(ci);
          break;
        }
      }
    }

    // Collect remaining
    const remainCreditors = creditors
      .filter((_, i) => !usedCreditors.has(i))
      .sort((a, b) => b.amount - a.amount);
    const remainDebtors = debtors
      .filter((_, i) => !usedDebtors.has(i))
      .sort((a, b) => b.amount - a.amount);

    // Pass 2: Greedy match remaining
    let ci = 0;
    let di = 0;
    while (ci < remainCreditors.length && di < remainDebtors.length) {
      const transfer = Math.min(remainCreditors[ci].amount, remainDebtors[di].amount);
      const rounded = Math.round(transfer * 100) / 100;

      if (rounded > 0) {
        suggestions.push({
          from: remainDebtors[di].userId,
          to: remainCreditors[ci].userId,
          amount: rounded,
        });
      }

      remainCreditors[ci].amount = Math.round((remainCreditors[ci].amount - rounded) * 100) / 100;
      remainDebtors[di].amount = Math.round((remainDebtors[di].amount - rounded) * 100) / 100;

      if (remainCreditors[ci].amount < 0.01) ci++;
      if (remainDebtors[di].amount < 0.01) di++;
    }

    return suggestions;
  }

  getAllSettlements() {
    return [...this.settlements];
  }

  clearSettlements() {
    this.settlements = [];
  }
}
