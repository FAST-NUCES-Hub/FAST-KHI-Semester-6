/**
 * Expense class - Manages expenses with equal, exact, and percentage split types.
 * Part of the Expense Management module.
 * 
 * Complex Algorithm #1: Expense splitting with three modes (equal, exact, percentage)
 * Each mode validates inputs and calculates individual shares correctly,
 * handling rounding issues for equal splits.
 */
export const SPLIT_TYPES = {
  EQUAL: 'equal',
  EXACT: 'exact',
  PERCENTAGE: 'percentage',
};

export class Expense {
  static #idCounter = 0;

  constructor({ description, amount, paidBy, splitType, splitDetails, groupId, participants }) {
    // Validate description
    if (!description || typeof description !== 'string' || description.trim().length === 0) {
      throw new Error('Expense description is required.');
    }

    // Validate amount
    if (amount === undefined || amount === null || typeof amount !== 'number') {
      throw new Error('Expense amount must be a number.');
    }
    if (amount <= 0) {
      throw new Error('Expense amount must be greater than zero.');
    }
    if (!Number.isFinite(amount)) {
      throw new Error('Expense amount must be a finite number.');
    }

    // Validate paidBy
    if (!paidBy) {
      throw new Error('paidBy (the user who paid) is required.');
    }

    // Validate splitType
    if (!Object.values(SPLIT_TYPES).includes(splitType)) {
      throw new Error(`Invalid split type: "${splitType}". Use: ${Object.values(SPLIT_TYPES).join(', ')}`);
    }

    // Validate participants
    if (!participants || !Array.isArray(participants) || participants.length === 0) {
      throw new Error('At least one participant is required.');
    }

    this.id = ++Expense.#idCounter;
    this.description = description.trim();
    this.amount = Math.round(amount * 100) / 100; // Round to 2 decimal places
    this.paidBy = paidBy;
    this.splitType = splitType;
    this.groupId = groupId;
    this.participants = participants;
    this.createdAt = new Date();

    // Calculate shares based on split type
    this.shares = this.#calculateShares(splitType, splitDetails, participants);
  }

  /**
   * COMPLEX ALGORITHM #1: Multi-mode Expense Splitting
   * 
   * Handles three splitting strategies:
   * - EQUAL: Divides evenly, distributes rounding remainder cent-by-cent
   * - EXACT: User-specified exact amounts that must sum to total
   * - PERCENTAGE: User-specified percentages that must sum to 100%
   */
  #calculateShares(splitType, splitDetails, participants) {
    const shares = new Map();

    switch (splitType) {
      case SPLIT_TYPES.EQUAL:
        return this.#calculateEqualSplit(participants, shares);

      case SPLIT_TYPES.EXACT:
        return this.#calculateExactSplit(splitDetails, participants, shares);

      case SPLIT_TYPES.PERCENTAGE:
        return this.#calculatePercentageSplit(splitDetails, participants, shares);

      default:
        throw new Error(`Unknown split type: ${splitType}`);
    }
  }

  #calculateEqualSplit(participants, shares) {
    const count = participants.length;
    const baseShare = Math.floor((this.amount * 100) / count) / 100;
    const remainder = Math.round((this.amount - baseShare * count) * 100);

    participants.forEach((userId, index) => {
      const share = index < remainder ? baseShare + 0.01 : baseShare;
      shares.set(userId, Math.round(share * 100) / 100);
    });

    return shares;
  }

  #calculateExactSplit(splitDetails, participants, shares) {
    if (!splitDetails || typeof splitDetails !== 'object') {
      throw new Error('Exact split requires splitDetails mapping userId to amount.');
    }

    let total = 0;
    participants.forEach((userId) => {
      const userAmount = splitDetails[userId];
      if (userAmount === undefined || userAmount === null) {
        throw new Error(`Missing exact amount for participant ${userId}.`);
      }
      if (typeof userAmount !== 'number' || userAmount < 0) {
        throw new Error(`Invalid exact amount for participant ${userId}. Must be a non-negative number.`);
      }
      total += userAmount;
      shares.set(userId, Math.round(userAmount * 100) / 100);
    });

    // Allow for small floating point differences
    if (Math.abs(total - this.amount) > 0.01) {
      throw new Error(
        `Exact split amounts (${total.toFixed(2)}) don't match expense total (${this.amount.toFixed(2)}).`
      );
    }

    return shares;
  }

  #calculatePercentageSplit(splitDetails, participants, shares) {
    if (!splitDetails || typeof splitDetails !== 'object') {
      throw new Error('Percentage split requires splitDetails mapping userId to percentage.');
    }

    let totalPercent = 0;
    participants.forEach((userId) => {
      const percent = splitDetails[userId];
      if (percent === undefined || percent === null) {
        throw new Error(`Missing percentage for participant ${userId}.`);
      }
      if (typeof percent !== 'number' || percent < 0 || percent > 100) {
        throw new Error(`Invalid percentage for participant ${userId}. Must be 0-100.`);
      }
      totalPercent += percent;
    });

    if (Math.abs(totalPercent - 100) > 0.01) {
      throw new Error(`Percentages must sum to 100%. Got: ${totalPercent.toFixed(2)}%.`);
    }

    participants.forEach((userId) => {
      const percent = splitDetails[userId];
      const share = Math.round(((this.amount * percent) / 100) * 100) / 100;
      shares.set(userId, share);
    });

    return shares;
  }

  getShareForUser(userId) {
    return this.shares.get(userId) || 0;
  }

  toJSON() {
    const sharesObj = {};
    this.shares.forEach((value, key) => {
      sharesObj[key] = value;
    });

    return {
      id: this.id,
      description: this.description,
      amount: this.amount,
      paidBy: this.paidBy,
      splitType: this.splitType,
      groupId: this.groupId,
      participants: [...this.participants],
      shares: sharesObj,
      createdAt: this.createdAt.toISOString(),
    };
  }

  static resetCounter() {
    Expense.#idCounter = 0;
  }
}
