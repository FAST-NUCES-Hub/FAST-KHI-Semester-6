# 📘 HOW.md — SplitEase Project Guide

## Project Overview

**SplitEase** is a smart expense-sharing platform (similar to Splitwise) built as a web application using **React + Vite**. It allows users to manage shared expenses within groups, calculate who owes whom, simplify debts, and record settlements.

**Student:** k232001  
**Course:** Software Engineering: Assignment 02  
**Framework:** React (Vite) + Jest for Testing

---

## Project Structure

```
SE_A02Q3_k232001/
├── src/
│   ├── core/                    # Business logic (OOP classes)
│   │   ├── User.js              # User Management module
│   │   ├── Group.js             # Group Management module
│   │   ├── Expense.js           # Expense Management module
│   │   ├── BalanceEngine.js     # Balance Calculation Engine
│   │   └── Settlement.js        # Settlement Module
│   ├── components/              # React UI components
│   │   ├── UserManagement.jsx   # User CRUD interface
│   │   ├── GroupManagement.jsx  # Group management interface
│   │   ├── ExpenseManagement.jsx# Expense adding/viewing
│   │   ├── BalanceDashboard.jsx # Balance visualization
│   │   ├── SettlementPanel.jsx  # Settlement recording
│   │   └── Notification.jsx     # Toast notifications
│   ├── store/
│   │   └── AppStore.jsx         # React Context state management
│   ├── __tests__/               # Automated test suites
│   │   ├── User.test.js         # Unit tests for User module
│   │   ├── Group.test.js        # Unit tests for Group module
│   │   ├── Expense.test.js      # Unit tests for Expense module
│   │   └── Integration.test.js  # Integration tests for Balance & Settlements
│   ├── App.jsx                  # Root application component
│   ├── main.jsx                 # Entry point
│   └── index.css                # Complete styling
├── docs/
│   ├── MANUAL_TEST_CASES.md     # Part 2: Manual test case design
│   └── TEST_REPORT.md           # Part 4: Test report
├── HOW.md                       # This file
├── index.html                   # HTML entry
├── package.json                 # Dependencies and scripts
├── jest.config.js               # Jest testing configuration
├── babel.config.json            # Babel transpiler config
└── vite.config.js               # Vite build config
```

---

## How to Run

### Prerequisites
- **Node.js** v18+ installed
- **npm** package manager

### Install Dependencies
```bash
npm install
```

### Run Development Server
```bash
npm run dev
```
Then open **http://localhost:5173** in your browser.

### Run Automated Tests
```bash
npm test
```

### Build for Production (optional)
```bash
npm run build
```

---

## Module Descriptions

### 1. User Management (`src/core/User.js`)

**What it does:** Creates and manages user accounts.

| Feature | Description |
|---------|-------------|
| Create User | Takes name, email, and optional contact numbers |
| Email Validation | Validates format and ensures uniqueness (case-insensitive) |
| Multiple Contacts | Each user can have multiple phone numbers (7-15 digits) |
| Add/Remove Contacts | Dynamically add or remove contact numbers |

**UI Location:** Top-left card → Click "**+ New User**" to create users.

---

### 2. Group Management (`src/core/Group.js`)

**What it does:** Creates groups and manages memberships.

| Feature | Description |
|---------|-------------|
| Create Group | Requires a name and a creator (who becomes admin) |
| Add Members | Add registered users to a group |
| Remove Members | Only admins can remove members |
| Admin Roles | Assign/rotate admin roles among members |
| Expand Groups | Click any group card to see members and manage them |

**UI Location:** Bottom-left card → Click "**+ New Group**" to create groups. Click a group card to expand it, add members, or manage admin roles. **The selected group is highlighted with a purple glow** — all expense/balance/settlement panels on the right react to the selected group.

---

### 3. Expense Management (`src/core/Expense.js`)

**What it does:** Adds expenses with three splitting strategies.

| Split Type | Description |
|-----------|-------------|
| **Equal** | Divides the total equally among all group members. Handles rounding (e.g., 100 ÷ 3 = 33.34, 33.33, 33.33) |
| **Exact** | You specify the exact amount each member owes. Must sum to the total. |
| **Percentage** | You specify what percentage each member pays. Must sum to 100%. |

**UI Location:** Top-right card → Select a group first, then click "**+ Add Expense**".

---

### 4. Balance Calculation Engine (`src/core/BalanceEngine.js`)

**What it does:** Calculates real-time financial positions for all group members.

| Feature | Description |
|---------|-------------|
| Net Balances | Shows each person's overall position (positive = gets money back, negative = owes money) |
| Simplified Debts | Uses a **greedy algorithm** to minimize the number of transactions needed to settle all debts |
| Detailed Debts | Shows the raw pairwise debt breakdown |

**UI Location:** Middle-right card → Shows automatically when a group with expenses is selected.

**How the Simplification Algorithm Works:**
1. Calculate net balance for each person
2. Separate into creditors (+) and debtors (−)
3. Sort by amount (largest first)
4. Greedily match the largest creditor with the largest debtor
5. Transfer the minimum of their amounts
6. Repeat until all settled

This reduces potentially O(n²) transactions to at most O(n−1).

---

### 5. Settlement Module (`src/core/Settlement.js`)

**What it does:** Records actual payments between users and updates balances dynamically.

| Feature | Description |
|---------|-------------|
| Record Payment | Log who paid whom and how much |
| Quick Settle | One-click settlement from suggested amounts |
| Suggestions | Smart algorithm suggests optimal settlements |
| History | Full audit trail of all settlements |

**UI Location:** Bottom-right card → Click "**+ Record Payment**" or use the "**✓ Settle**" quick buttons on suggested settlements.

---

## Complex Algorithms Implemented

### Algorithm 1: Multi-Mode Expense Splitting
**File:** `src/core/Expense.js` → `#calculateShares()`

Handles three splitting strategies with proper edge case handling:
- **Equal split** with rounding remainder distribution (cent-by-cent to first users)
- **Exact split** with sum validation (must match total)
- **Percentage split** with 100% validation

### Algorithm 2: Debt Simplification (Greedy Algorithm)
**File:** `src/core/BalanceEngine.js` → `simplifyDebts()`

Minimizes number of transactions using a greedy matching approach:
- Computes net balance per person
- Separates into creditors/debtors
- Matches largest creditor with largest debtor
- Guarantees ≤ (n−1) transactions for n people

### Algorithm 3: Smart Settlement Suggestion
**File:** `src/core/Settlement.js` → `SettlementManager.suggestSettlements()`

Enhanced settlement suggestion with two-pass approach:
1. **Pass 1:** Find exact amount matches (optimal pairing)
2. **Pass 2:** Greedy matching for remaining debts
Handles circular debts, partial settlements, and already-balanced groups.

---

## Typical Usage Flow

1. **Create Users** → Add 3+ friends (Ali, Sara, Ahmed)
2. **Create a Group** → Name it (e.g., "Weekend Trip"), select a creator
3. **Add Members** → Expand the group and add all friends
4. **Add Expenses** → Select the group, add expenses with split types
5. **View Balances** → See who owes whom in the Balance Dashboard
6. **Settle Up** → Use suggestions or manually record payments
7. **Verify** → Balances update in real-time after settlements

---

## Testing

- **35 automated tests** across 4 test suites (Unit + Integration)
- **Comprehensive manual test cases** documented in `docs/MANUAL_TEST_CASES.md`
- **Full test report** in `docs/TEST_REPORT.md`

Run tests: `npm test`

---

## Technology Decisions

| Choice | Rationale |
|--------|-----------|
| **React + Vite** | Fast development, component-based architecture, easy testing with Jest |
| **Vanilla CSS** | Full control over design, no utility class overhead |
| **Jest** | Industry-standard JS testing, works with React ecosystem |
| **Context API** | Lightweight state management without external dependencies |
| **OOP Core Classes** | Clean separation of business logic from UI, easy unit testing |
