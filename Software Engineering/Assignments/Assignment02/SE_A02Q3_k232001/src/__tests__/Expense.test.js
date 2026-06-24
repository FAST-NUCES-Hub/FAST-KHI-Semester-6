/**
 * Automated Tests — Part 3
 * 
 * Unit Tests for Expense Management Module
 */
import { Expense, SPLIT_TYPES } from '../core/Expense';

describe('Expense Management Module', () => {
  beforeEach(() => {
    Expense.resetCounter();
  });

  // TEST 19: Equal split
  test('TC-A19: should correctly split expense equally among 3 participants', () => {
    const expense = new Expense({
      description: 'Dinner',
      amount: 3000,
      paidBy: 1,
      splitType: SPLIT_TYPES.EQUAL,
      participants: [1, 2, 3],
    });

    expect(expense.getShareForUser(1)).toBe(1000);
    expect(expense.getShareForUser(2)).toBe(1000);
    expect(expense.getShareForUser(3)).toBe(1000);
  });

  // TEST 20: Equal split with rounding
  test('TC-A20: should handle rounding correctly in equal split (e.g. 100 / 3)', () => {
    const expense = new Expense({
      description: 'Coffee',
      amount: 100,
      paidBy: 1,
      splitType: SPLIT_TYPES.EQUAL,
      participants: [1, 2, 3],
    });

    const total = expense.getShareForUser(1) + expense.getShareForUser(2) + expense.getShareForUser(3);
    expect(total).toBeCloseTo(100, 1);
    // First user(s) get the extra penny
    expect(expense.getShareForUser(1)).toBe(33.34);
    expect(expense.getShareForUser(2)).toBe(33.33);
    expect(expense.getShareForUser(3)).toBe(33.33);
  });

  // TEST 21: Exact split
  test('TC-A21: should correctly handle exact split amounts', () => {
    const expense = new Expense({
      description: 'Mixed bill',
      amount: 5000,
      paidBy: 1,
      splitType: SPLIT_TYPES.EXACT,
      splitDetails: { 1: 2000, 2: 1500, 3: 1500 },
      participants: [1, 2, 3],
    });

    expect(expense.getShareForUser(1)).toBe(2000);
    expect(expense.getShareForUser(2)).toBe(1500);
    expect(expense.getShareForUser(3)).toBe(1500);
  });

  // TEST 22: Exact amounts mismatch
  test('TC-A22: should reject exact split when amounts do not match total', () => {
    expect(() => {
      new Expense({
        description: 'Invalid',
        amount: 5000,
        paidBy: 1,
        splitType: SPLIT_TYPES.EXACT,
        splitDetails: { 1: 1000, 2: 1000, 3: 1000 },
        participants: [1, 2, 3],
      });
    }).toThrow("don't match expense total");
  });

  // TEST 23: Percentage split
  test('TC-A23: should correctly split by percentage', () => {
    const expense = new Expense({
      description: 'Percentage test',
      amount: 10000,
      paidBy: 1,
      splitType: SPLIT_TYPES.PERCENTAGE,
      splitDetails: { 1: 50, 2: 30, 3: 20 },
      participants: [1, 2, 3],
    });

    expect(expense.getShareForUser(1)).toBe(5000);
    expect(expense.getShareForUser(2)).toBe(3000);
    expect(expense.getShareForUser(3)).toBe(2000);
  });

  // TEST 24: Percentages not summing to 100
  test('TC-A24: should reject percentages not summing to 100%', () => {
    expect(() => {
      new Expense({
        description: 'Bad percent',
        amount: 1000,
        paidBy: 1,
        splitType: SPLIT_TYPES.PERCENTAGE,
        splitDetails: { 1: 50, 2: 30 },
        participants: [1, 2],
      });
    }).toThrow('must sum to 100%');
  });

  // TEST 25: Zero/negative amount (boundary test)
  test('TC-A25: should reject zero and negative expense amounts', () => {
    expect(() => {
      new Expense({
        description: 'Zero',
        amount: 0,
        paidBy: 1,
        splitType: SPLIT_TYPES.EQUAL,
        participants: [1, 2],
      });
    }).toThrow('greater than zero');

    expect(() => {
      new Expense({
        description: 'Negative',
        amount: -500,
        paidBy: 1,
        splitType: SPLIT_TYPES.EQUAL,
        participants: [1, 2],
      });
    }).toThrow('greater than zero');
  });

  // TEST 26: Invalid split type
  test('TC-A26: should reject invalid split types', () => {
    expect(() => {
      new Expense({
        description: 'Bad type',
        amount: 1000,
        paidBy: 1,
        splitType: 'random',
        participants: [1, 2],
      });
    }).toThrow('Invalid split type');
  });

  // TEST 27: Missing description
  test('TC-A27: should reject expense with missing description', () => {
    expect(() => {
      new Expense({
        description: '',
        amount: 1000,
        paidBy: 1,
        splitType: SPLIT_TYPES.EQUAL,
        participants: [1, 2],
      });
    }).toThrow('description is required');
  });
});
