# 📊 Test Report — Part 4

## Smart Expense Sharing System (SplitEase)
**Student:** k232001 | **Course:** Software Engineering: Assignment 02

---

## 1. Approach and Understanding of the Problem Statement

### Problem Understanding

The assignment requires building a **mini expense-sharing platform** (similar to Splitwise) that handles:
- **User Management** with multi-contact support and unique email validation
- **Group Management** with member add/remove and admin role assignment
- **Expense Management** supporting three split modes: equal, exact, and percentage
- **Balance Calculation** that shows who owes whom with debt simplification
- **Settlement Recording** that updates balances dynamically

### Design Approach

I chose a **modular OOP architecture** where business logic is completely separated from the UI layer:

```
Business Logic Layer (src/core/)     ←→     UI Layer (src/components/)
  ├── User.js                                ├── UserManagement.jsx
  ├── Group.js                               ├── GroupManagement.jsx
  ├── Expense.js                             ├── ExpenseManagement.jsx
  ├── BalanceEngine.js                       ├── BalanceDashboard.jsx
  └── Settlement.js                          └── SettlementPanel.jsx
```

This separation was a deliberate design decision because:
1. **Testability**: Core logic classes can be tested in isolation without React/DOM dependencies
2. **Maintainability**: Business rules can change without UI modifications and vice versa
3. **Reusability**: The same core classes could power a CLI tool, mobile app, or API

### Technology Choice

| Technology | Reasoning |
|-----------|-----------|
| **React (Vite)** | Component-based architecture naturally maps to the 5 modules. Vite provides instant HMR for rapid development. |
| **Jest** | Jest is the standard testing framework for JavaScript/React projects, providing both unit and integration test capabilities. |
| **Vanilla CSS** | Full design control without framework overhead. Enables the glassmorphism dark theme. |
| **Context API** | Lightweight state management—fits our needs without Redux/Zustand complexity. |

### Complex Algorithms

Three complex algorithms were implemented:

1. **Multi-Mode Expense Splitting** (`Expense.js`):
   - Equal split with rounding remainder distribution
   - Exact split with sum validation
   - Percentage split with 100% validation
   
2. **Debt Simplification** (`BalanceEngine.js`):
   - Greedy algorithm that computes net balances, separates creditors/debtors, and matches them to minimize transactions
   - Reduces O(n²) potential transactions to O(n-1)
   - Handles circular debts (everyone's net zero → zero transactions)

3. **Smart Settlement Suggestion** (`Settlement.js`):
   - Two-pass algorithm: first finds exact amount matches, then greedy-matches remainder
   - Handles partial settlements, circular debts, and already-settled groups

---

## 2. Why Specific Test Cases Were Chosen

### User Management Tests (TC-A01 to TC-A10)

| Test Focus | Why This Was Chosen |
|-----------|---------------------|
| **Valid creation** (TC-A01) | Happy path — ensures basic functionality works |
| **Duplicate email** (TC-A02) | Critical business rule — prevents identity conflicts |
| **Invalid email format** (TC-A03) | Input validation — most common error users make |
| **Empty name** (TC-A04) | Boundary — empty string and null inputs |
| **Multiple contacts** (TC-A05) | Feature verification — multi-contact is a core feature |
| **Invalid short contact** (TC-A06) | Boundary — tests minimum length validation (7 digits) |
| **Duplicate contact** (TC-A07) | Data integrity — prevents duplicates in contact list |
| **Remove contact** (TC-A08) | CRUD completeness — tests the "delete" operation |
| **JSON serialization** (TC-A09) | Integration readiness — ensures data can be exported |
| **Case-insensitive email** (TC-A10) | Edge case — "ALI@email.com" and "ali@email.com" should be treated the same |

### Group Management Tests (TC-A11 to TC-A18)

| Test Focus | Why This Was Chosen |
|-----------|---------------------|
| **Create with admin** (TC-A11) | Verifies creator gets automatic member+admin status |
| **Add members** (TC-A12) | Core CRUD operation for groups |
| **Duplicate prevention** (TC-A13) | Data integrity guard |
| **Admin removes member** (TC-A14) | Authorization logic — admin-only operation |
| **Non-admin removal blocked** (TC-A15) | Security — access control enforcement |
| **Admin assignment** (TC-A16) | Role management feature |
| **Empty name** (TC-A17) | Input validation boundary |
| **Self-removal block** (TC-A18) | Edge case — prevents orphaned admin-less groups |

### Expense Management Tests (TC-A19 to TC-A27)

| Test Focus | Why This Was Chosen |
|-----------|---------------------|
| **Equal split** (TC-A19) | Most common split type — must be accurate |
| **Rounding (100÷3)** (TC-A20) | Classic edge case — floating point handling |
| **Exact split** (TC-A21) | Second split mode verification |
| **Exact mismatch** (TC-A22) | Validation — amounts must sum to total |
| **Percentage split** (TC-A23) | Third split mode verification |
| **Percentage ≠ 100** (TC-A24) | Validation — percentages must sum to 100% |
| **Zero/negative amount** (TC-A25) | Boundary — financial amounts must be positive |
| **Invalid split type** (TC-A26) | Equivalence partitioning — invalid input class |
| **Missing description** (TC-A27) | Required field validation |

### Integration Tests (TC-A28 to TC-A35)

| Test Focus | Why This Was Chosen |
|-----------|---------------------|
| **Assignment example** (TC-A28) | Directly verifies the example from the assignment brief |
| **Debt simplification** (TC-A29) | Tests the greedy algorithm for minimum transactions |
| **Circular debts** (TC-A30) | Edge case — A→B→C→A cycle should cancel out |
| **Partial settlement** (TC-A31) | Real-world scenario — people don't always settle fully |
| **Full settlement** (TC-A32) | Verifies complete debt clearing |
| **Smart suggestions** (TC-A33) | Tests the settlement recommendation algorithm |
| **Self-settlement** (TC-A34) | Edge case — meaningless operation blocked |
| **Zero/negative settlement** (TC-A35) | Boundary — invalid financial amounts |

---

## 3. Challenges in Testing Logic

### Challenge 1: Floating Point Arithmetic
**Problem:** JavaScript floating point math causes issues like `0.1 + 0.2 = 0.30000000000000004`

**Solution:** All monetary calculations use `Math.round(value * 100) / 100` to ensure 2 decimal place precision. Tests use `toBeCloseTo()` for floating-point comparisons where exact matching isn't possible.

**Example:** Splitting 100 among 3 people:
- Naive: 33.33 + 33.33 + 33.33 = 99.99 (lost 1 cent!)
- Our approach: 33.34 + 33.33 + 33.33 = 100.00 (remainder distributed)

### Challenge 2: Private Class Fields (#) in Tests
**Problem:** JavaScript private class fields (`#idCounter`, `#emailRegistry`) cannot be accessed from test code, making state verification difficult.

**Solution:** Added `static resetRegistry()` and `static resetCounter()` methods to each class, called in `beforeEach()` blocks. This allows tests to run independently without state leakage between test cases.

### Challenge 3: Circular Debt Detection
**Problem:** When A owes B, B owes C, and C owes A with equal amounts, the system should recognize that no actual money needs to change hands.

**Solution:** The greedy algorithm naturally handles this because net balances for all participants come out to zero, resulting in an empty simplified transaction list. Test TC-A30 specifically validates this.

### Challenge 4: Testing State-Dependent Modules
**Problem:** The BalanceEngine depends on Expense objects, and the SettlementManager depends on net balances — testing requires proper setup.

**Solution:** Integration tests construct the full dependency chain (create expenses → compute balances → apply settlements → verify updated balances). This ensures modules work together correctly, not just in isolation.

### Challenge 5: Rounding Remainder Distribution
**Problem:** When distributing cents from rounding, the order in which participants receive the extra cent matters for deterministic testing.

**Solution:** We consistently assign extra cents to the first participants in the array order. Tests verify specific per-user amounts rather than just the total, ensuring deterministic behavior.

---

## 4. Comparison: Manual vs Automated Testing

| Aspect | Manual Testing | Automated Testing |
|--------|---------------|-------------------|
| **Speed** | Slow — each test requires human interaction with the UI | Fast — 35 tests run in ~3 seconds |
| **Repeatability** | Error-prone — human may miss steps or make mistakes | 100% repeatable — same inputs, same execution |
| **Coverage** | Good for UX/visual testing and exploratory testing | Excellent for logic validation and regression |
| **Cost** | High ongoing cost — must re-execute for every change | High initial cost, low ongoing cost |
| **UI Testing** | ✅ Can verify visual layout, animations, responsiveness | ❌ Cannot easily verify visual appearance |
| **Edge Cases** | Takes time to set up boundary conditions | Easy — just pass different values |
| **Integration** | ✅ Tests full user workflow end-to-end | ✅ Integration tests verify module interactions |
| **Discovery** | ✅ Can uncover unexpected UX issues | ❌ Only tests what's explicitly coded |
| **Maintenance** | Low — test cases are documentation | Medium — tests must be updated with code changes |

### When Manual Testing Was More Valuable

1. **UI Layout Verification**: Checking that forms appear correctly, cards are aligned, responsive design works
2. **Animation Smoothness**: Verifying slide-in animations, glow effects, hover transitions
3. **Notification Behavior**: Ensuring toast notifications appear and disappear at the right time
4. **Workflow Usability**: Confirming the "create user → create group → add members → add expense" flow feels intuitive
5. **Cross-Browser Rendering**: Checking the glassmorphism effects work across browsers

### When Automated Testing Was More Valuable

1. **Expense Splitting Math**: Ensuring 3000÷3 = 1000 exactly, every time
2. **Rounding Edge Cases**: Verifying 100÷3 distributes the extra cent correctly
3. **Validation Rules**: Testing all invalid input combinations (empty name, bad email, negative amount, etc.)
4. **Debt Simplification**: Confirming the algorithm produces minimum transactions
5. **Circular Debt Handling**: Verifying that A→B→C→A debts cancel to zero
6. **Regression**: After any code change, all 35 tests re-run in seconds

### Conclusion

**Both testing approaches are complementary.** Manual testing excels at verifying user experience and visual correctness, while automated testing excels at verifying business logic correctness and preventing regressions. In a production system, I would use:
- **Automated unit/integration tests** for all business logic (run on every commit)
- **Manual testing** for UX verification during sprint reviews
- **Automated E2E tests** (e.g., Cypress/Playwright) to bridge the gap and test user workflows automatically

---

## Test Execution Summary

### Automated Tests (35 tests, 4 suites)

```
Test Suites: 4 passed, 4 total
Tests:       35 passed, 35 total
Snapshots:   0 total
Time:        ~3.3 seconds
```

| Suite | Tests | Status |
|-------|-------|--------|
| User Management | 10 | ✅ All Passed |
| Group Management | 8 | ✅ All Passed |
| Expense Management | 9 | ✅ All Passed |
| Integration (Balance + Settlement) | 8 | ✅ All Passed |

### Manual Tests (56 test cases)

| Module | Tests | Passed | Failed |
|--------|-------|--------|--------|
| User Management | 17 | 17 | 0 |
| Group Management | 10 | 10 | 0 |
| Expense Management | 15 | 15 | 0 |
| Balance Calculation | 7 | 7 | 0 |
| Settlement | 7 | 7 | 0 |
| **Total** | **56** | **56** | **0** |
