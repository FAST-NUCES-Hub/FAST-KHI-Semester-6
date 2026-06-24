/**
 * BalanceEngine - Calculates net balances and who owes whom.
 * 
 * Complex Algorithm #2: Net Balance Calculation & Debt Simplification
 * 
 * This engine processes all expenses and settlements to calculate:
 * 1. Pairwise debts (who owes whom and how much)
 * 2. Net balances (each person's overall position)
 * 3. Simplified debts (minimize number of transactions using greedy algorithm)
 * 
 * The debt simplification algorithm works by:
 * - Computing net balances for each user
 * - Separating users into creditors (positive balance) and debtors (negative balance)
 * - Greedily matching the largest creditor with the largest debtor
 * - This reduces O(n²) potential transactions to at most O(n-1)
 */
export class BalanceEngine {
  /**
   * Calculate raw pairwise balances from expenses and settlements.
   * Returns a Map of Maps: balances[fromId][toId] = amount owed
   */
  static calculatePairwiseBalances(expenses, settlements = []) {
    // balances[A][B] > 0 means A owes B that amount
    const balances = new Map();

    const ensureEntry = (from, to) => {
      if (!balances.has(from)) balances.set(from, new Map());
      if (!balances.get(from).has(to)) balances.get(from).set(to, 0);
    };

    // Process each expense
    expenses.forEach((expense) => {
      const payerId = expense.paidBy;
      expense.shares.forEach((share, userId) => {
        if (userId !== payerId && share > 0) {
          ensureEntry(userId, payerId);
          ensureEntry(payerId, userId);
          // userId owes payerId
          const currentOwed = balances.get(userId).get(payerId);
          balances.get(userId).set(payerId, Math.round((currentOwed + share) * 100) / 100);
        }
      });
    });

    // Process settlements (reduce debts)
    settlements.forEach((settlement) => {
      const { fromUserId, toUserId, amount } = settlement;
      ensureEntry(fromUserId, toUserId);
      ensureEntry(toUserId, fromUserId);
      const currentOwed = balances.get(fromUserId).get(toUserId);
      balances.get(fromUserId).set(toUserId, Math.round((currentOwed - amount) * 100) / 100);
    });

    return balances;
  }

  /**
   * Calculate net balances: positive means others owe you, negative means you owe others.
   */
  static calculateNetBalances(expenses, settlements = []) {
    const netBalances = new Map();

    const addToBalance = (userId, amount) => {
      const current = netBalances.get(userId) || 0;
      netBalances.set(userId, Math.round((current + amount) * 100) / 100);
    };

    // Process expenses
    expenses.forEach((expense) => {
      const payerId = expense.paidBy;
      // Payer paid the full amount
      addToBalance(payerId, expense.amount);
      // Each participant (including payer) owes their share
      expense.shares.forEach((share, userId) => {
        addToBalance(userId, -share);
      });
    });

    // Process settlements
    settlements.forEach((settlement) => {
      addToBalance(settlement.fromUserId, settlement.amount); // settler reduces their debt
      addToBalance(settlement.toUserId, -settlement.amount); // receiver's credit decreases
    });

    return netBalances;
  }

  /**
   * COMPLEX ALGORITHM #2: Debt Simplification (Greedy Matching)
   * 
   * Minimizes the number of transactions needed to settle all debts.
   * 
   * Algorithm:
   * 1. Compute net balance for each person
   * 2. Separate into creditors (net positive) and debtors (net negative)
   * 3. Sort both lists by absolute value (descending)
   * 4. Match largest creditor with largest debtor
   * 5. The smaller of the two amounts is the transfer amount
   * 6. Repeat until all settled
   * 
   * Time Complexity: O(n log n) for sorting + O(n) for matching = O(n log n)
   * This guarantees at most (n-1) transactions for n people.
   */
  static simplifyDebts(expenses, settlements = []) {
    const netBalances = BalanceEngine.calculateNetBalances(expenses, settlements);
    const creditors = []; // people who are owed money (positive balance)
    const debtors = []; // people who owe money (negative balance)

    netBalances.forEach((balance, userId) => {
      const roundedBal = Math.round(balance * 100) / 100;
      if (roundedBal > 0.005) {
        creditors.push({ userId, amount: roundedBal });
      } else if (roundedBal < -0.005) {
        debtors.push({ userId, amount: -roundedBal }); // store as positive
      }
    });

    // Sort by amount descending (greedily match largest first)
    creditors.sort((a, b) => b.amount - a.amount);
    debtors.sort((a, b) => b.amount - a.amount);

    const simplifiedTransactions = [];
    let ci = 0;
    let di = 0;

    while (ci < creditors.length && di < debtors.length) {
      const creditor = creditors[ci];
      const debtor = debtors[di];
      const transferAmount = Math.min(creditor.amount, debtor.amount);
      const roundedTransfer = Math.round(transferAmount * 100) / 100;

      if (roundedTransfer > 0) {
        simplifiedTransactions.push({
          from: debtor.userId,
          to: creditor.userId,
          amount: roundedTransfer,
        });
      }

      creditor.amount = Math.round((creditor.amount - roundedTransfer) * 100) / 100;
      debtor.amount = Math.round((debtor.amount - roundedTransfer) * 100) / 100;

      if (creditor.amount < 0.005) ci++;
      if (debtor.amount < 0.005) di++;
    }

    return simplifiedTransactions;
  }

  /**
   * Get detailed "who owes whom" list without simplification.
   */
  static getDetailedDebts(expenses, settlements = []) {
    const pairwise = BalanceEngine.calculatePairwiseBalances(expenses, settlements);
    const debts = [];

    const processed = new Set();

    pairwise.forEach((owedMap, fromId) => {
      owedMap.forEach((amount, toId) => {
        const pairKey = [Math.min(fromId, toId), Math.max(fromId, toId)].join('-');
        if (processed.has(pairKey)) return;
        processed.add(pairKey);

        const reverseAmount = pairwise.get(toId)?.get(fromId) || 0;
        const netAmount = Math.round((amount - reverseAmount) * 100) / 100;

        if (netAmount > 0.005) {
          debts.push({ from: fromId, to: toId, amount: netAmount });
        } else if (netAmount < -0.005) {
          debts.push({ from: toId, to: fromId, amount: -netAmount });
        }
      });
    });

    return debts;
  }
}
