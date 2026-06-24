/**
 * Automated Tests — Part 3
 * 
 * Integration Tests for Balance Calculation Engine & Settlement Module
 * These test the interaction between Expense, BalanceEngine, and Settlement modules.
 */
import { Expense, SPLIT_TYPES } from '../core/Expense';
import { BalanceEngine } from '../core/BalanceEngine';
import { Settlement, SettlementManager } from '../core/Settlement';

describe('Balance Calculation Engine — Integration Tests', () => {
  beforeEach(() => {
    Expense.resetCounter();
    Settlement.resetCounter();
  });

  // TEST 28: Net balances for example scenario (Ali pays 3000 dinner, Sara pays 1500 fuel)
  test('TC-A28: should calculate correct net balances for the assignment example', () => {
    // Ali=1, Sara=2, Ahmed=3
    const expenses = [
      new Expense({
        description: 'Dinner',
        amount: 3000,
        paidBy: 1,
        splitType: SPLIT_TYPES.EQUAL,
        participants: [1, 2, 3],
      }),
      new Expense({
        description: 'Fuel',
        amount: 1500,
        paidBy: 2,
        splitType: SPLIT_TYPES.EQUAL,
        participants: [1, 2, 3],
      }),
    ];

    const netBalances = BalanceEngine.calculateNetBalances(expenses);
    
    // Ali paid 3000, owes 1000 (dinner) + 500 (fuel) = 1500. Net = +1500
    // Sara paid 1500, owes 1000 (dinner) + 500 (fuel) = 1500. Net = 0
    // Ahmed paid 0, owes 1000 (dinner) + 500 (fuel) = 1500. Net = -1500
    expect(netBalances.get(1)).toBe(1500);  // Ali gets back 1500
    expect(netBalances.get(2)).toBe(0);      // Sara is settled
    expect(netBalances.get(3)).toBe(-1500);  // Ahmed owes 1500
  });

  // TEST 29: Simplified debts should minimize transactions
  test('TC-A29: should simplify debts to minimum transactions', () => {
    const expenses = [
      new Expense({
        description: 'Dinner',
        amount: 3000,
        paidBy: 1,
        splitType: SPLIT_TYPES.EQUAL,
        participants: [1, 2, 3],
      }),
      new Expense({
        description: 'Fuel',
        amount: 1500,
        paidBy: 2,
        splitType: SPLIT_TYPES.EQUAL,
        participants: [1, 2, 3],
      }),
    ];

    const simplified = BalanceEngine.simplifyDebts(expenses);
    
    // Only one transaction needed: Ahmed pays Ali 1500
    expect(simplified).toHaveLength(1);
    expect(simplified[0].from).toBe(3);   // Ahmed
    expect(simplified[0].to).toBe(1);     // Ali
    expect(simplified[0].amount).toBe(1500);
  });

  // TEST 30: Circular debts
  test('TC-A30: should handle circular debts correctly', () => {
    // A pays for B, B pays for C, C pays for A
    const expenses = [
      new Expense({
        description: 'A pays for A,B',
        amount: 2000,
        paidBy: 1,
        splitType: SPLIT_TYPES.EQUAL,
        participants: [1, 2],
      }),
      new Expense({
        description: 'B pays for B,C',
        amount: 2000,
        paidBy: 2,
        splitType: SPLIT_TYPES.EQUAL,
        participants: [2, 3],
      }),
      new Expense({
        description: 'C pays for C,A',
        amount: 2000,
        paidBy: 3,
        splitType: SPLIT_TYPES.EQUAL,
        participants: [3, 1],
      }),
    ];

    const netBalances = BalanceEngine.calculateNetBalances(expenses);
    
    // Each person paid 2000 and owes 2000 total, net should be 0
    expect(netBalances.get(1)).toBe(0);
    expect(netBalances.get(2)).toBe(0);
    expect(netBalances.get(3)).toBe(0);

    const simplified = BalanceEngine.simplifyDebts(expenses);
    expect(simplified).toHaveLength(0); // No transactions needed!
  });

  // TEST 31: Settlement updates balances
  test('TC-A31: should update balances after settlement (partial settlement)', () => {
    const expenses = [
      new Expense({
        description: 'Dinner',
        amount: 3000,
        paidBy: 1,
        splitType: SPLIT_TYPES.EQUAL,
        participants: [1, 2, 3],
      }),
    ];

    // Ahmed (3) partially settles 500 to Ali (1)
    const settlements = [
      new Settlement({ fromUserId: 3, toUserId: 1, amount: 500, groupId: 1 }),
    ];

    const netAfter = BalanceEngine.calculateNetBalances(expenses, settlements);
    
    // Ali: paid 3000, share 1000, gets 500 settlement. Net = +1500
    // Ahmed: paid 0, share 1000, paid 500 settlement. Net = -500
    expect(netAfter.get(1)).toBe(1500);   // Ali still gets back 1500 -> actually 2000-500=1500
    expect(netAfter.get(3)).toBe(-500);   // Ahmed now owes only 500
  });

  // TEST 32: Full settlement clears balances
  test('TC-A32: should show zero balances after full settlement', () => {
    const expenses = [
      new Expense({
        description: 'Dinner',
        amount: 3000,
        paidBy: 1,
        splitType: SPLIT_TYPES.EQUAL,
        participants: [1, 2, 3],
      }),
    ];

    const settlements = [
      new Settlement({ fromUserId: 2, toUserId: 1, amount: 1000, groupId: 1 }),
      new Settlement({ fromUserId: 3, toUserId: 1, amount: 1000, groupId: 1 }),
    ];

    const netAfter = BalanceEngine.calculateNetBalances(expenses, settlements);
    
    expect(netAfter.get(1)).toBe(0);
    expect(netAfter.get(2)).toBe(0);
    expect(netAfter.get(3)).toBe(0);
  });

  // TEST 33: Settlement manager suggestions
  test('TC-A33: Settlement manager should suggest optimal settlements', () => {
    const manager = new SettlementManager();
    
    const netBalances = new Map();
    netBalances.set(1, 2000);   // Ali is owed 2000
    netBalances.set(2, -800);   // Sara owes 800
    netBalances.set(3, -1200);  // Ahmed owes 1200

    const suggestions = manager.suggestSettlements(netBalances);
    
    // Should suggest minimum transactions
    expect(suggestions.length).toBeLessThanOrEqual(2);
    
    // Total suggested amount should equal total debt
    const totalSuggested = suggestions.reduce((sum, s) => sum + s.amount, 0);
    expect(totalSuggested).toBe(2000);
  });

  // TEST 34: Self-settlement rejection
  test('TC-A34: should reject settlement to yourself', () => {
    expect(() => {
      new Settlement({ fromUserId: 1, toUserId: 1, amount: 100, groupId: 1 });
    }).toThrow('Cannot settle with yourself');
  });

  // TEST 35: Zero/negative settlement amount
  test('TC-A35: should reject zero and negative settlement amounts', () => {
    expect(() => {
      new Settlement({ fromUserId: 1, toUserId: 2, amount: 0, groupId: 1 });
    }).toThrow('greater than zero');

    expect(() => {
      new Settlement({ fromUserId: 1, toUserId: 2, amount: -100, groupId: 1 });
    }).toThrow('greater than zero');
  });
});
