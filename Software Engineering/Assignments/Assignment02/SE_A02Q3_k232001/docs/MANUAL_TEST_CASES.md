# 📋 Manual Test Cases — Part 2

## Smart Expense Sharing System (SplitEase)
**Student:** k232001 | **Course:** Software Engineering: Assignment 02

---

## 1. User Management Test Cases

### Functional Testing

| Test ID | Description | Input | Expected Output | Observed Output | Status |
|---------|-------------|-------|-----------------|-----------------|--------|
| TC-M01 | Create user with valid data | Name: "Ali Khan", Email: "ali@email.com", Contact: "03001234567" | User created with ID, name, email, and contact number stored | User "Ali Khan" created successfully with all fields populated | ✅ Pass |
| TC-M02 | Create user without contact number | Name: "Sara Ahmed", Email: "sara@email.com", Contacts: (empty) | User created with empty contacts array | User created with zero contact numbers | ✅ Pass |
| TC-M03 | Create user with multiple contacts | Name: "Ahmed Raza", Email: "ahmed@email.com", Contacts: "03111111111, 03222222222" | User created with 2 contact numbers | Both contacts stored and displayed | ✅ Pass |
| TC-M04 | Reject duplicate email | Name: "Ali 2", Email: "ali@email.com" (already exists) | Error: "Email already registered" | Error notification shown: email already registered | ✅ Pass |
| TC-M05 | Reject invalid email format | Name: "Test", Email: "notanemail" | Error: "A valid email address is required" | Error notification: invalid email | ✅ Pass |
| TC-M06 | Reject empty name | Name: "", Email: "test@email.com" | Error: "User name is required" | HTML required validation prevents submission | ✅ Pass |
| TC-M07 | Email case insensitivity | Create "user1@Email.COM", then try "user1@email.com" | Second creation rejected as duplicate | Error: email already registered | ✅ Pass |

### Boundary Testing

| Test ID | Description | Input | Expected Output | Observed Output | Status |
|---------|-------------|-------|-----------------|-----------------|--------|
| TC-M08 | Single character name | Name: "A", Email: "a@b.com" | User created (valid single-char name) | User "A" created successfully | ✅ Pass |
| TC-M09 | Very long name (100+ chars) | Name: "A" repeated 150 times, Email: "long@email.com" | User created (no max length imposed) | User created with full name stored | ✅ Pass |
| TC-M10 | Contact number exactly 7 digits | Contact: "1234567" | Valid — minimum length accepted | Contact stored successfully | ✅ Pass |
| TC-M11 | Contact number exactly 15 digits | Contact: "123456789012345" | Valid — maximum length accepted | Contact stored successfully | ✅ Pass |
| TC-M12 | Contact number 6 digits (below min) | Contact: "123456" | Error: Invalid contact number | Error notification shown | ✅ Pass |
| TC-M13 | Contact number 16 digits (above max) | Contact: "1234567890123456" | Error: Invalid contact number | Error notification shown | ✅ Pass |

### Equivalence Partitioning

| Test ID | Description | Input Class | Input | Expected Output | Observed Output | Status |
|---------|-------------|-------------|-------|-----------------|-----------------|--------|
| TC-M14 | Valid email class | Valid | "user@domain.com" | User created | User created | ✅ Pass |
| TC-M15 | Invalid email — no @ | Invalid | "userdomain.com" | Rejected | Error notification | ✅ Pass |
| TC-M16 | Invalid email — no domain | Invalid | "user@" | Rejected | Error notification | ✅ Pass |
| TC-M17 | Invalid email — empty string | Invalid | "" | Rejected | HTML required validation | ✅ Pass |

---

## 2. Group Management Test Cases

### Functional Testing

| Test ID | Description | Input | Expected Output | Observed Output | Status |
|---------|-------------|-------|-----------------|-----------------|--------|
| TC-M18 | Create group with valid creator | Group: "Weekend Trip", Creator: Ali (existing user) | Group created, creator as member+admin | Group created with 1 member (admin) | ✅ Pass |
| TC-M19 | Add member to group | Group: "Weekend Trip", Add: Sara | Sara added to group, member count increases | Sara appears in member list | ✅ Pass |
| TC-M20 | Add duplicate member | Try adding Sara again to same group | Error: "User already a member" | Error notification shown | ✅ Pass |
| TC-M21 | Remove member (as admin) | Admin removes Sara from group | Sara removed, member count decreases | Sara removed from member list | ✅ Pass |
| TC-M22 | Remove member (as non-admin) | Non-admin tries to remove a member | Error: "Only admins can remove members" | Error notification shown | ✅ Pass |
| TC-M23 | Assign admin role | Admin assigns Sara as admin | Sara gets admin badge | Admin badge appears next to Sara | ✅ Pass |
| TC-M24 | Create group without users | Click "New Group" with 0 users | Button disabled or error shown | Button disabled with warning message | ✅ Pass |

### Boundary Testing

| Test ID | Description | Input | Expected Output | Observed Output | Status |
|---------|-------------|-------|-----------------|-----------------|--------|
| TC-M25 | Group with 1 member (creator only) | Create group, don't add anyone else | Group created with 1 member | Group card shows "1 members" | ✅ Pass |
| TC-M26 | Empty group name | Group name: "" | Error: "Group name is required" | HTML required validation prevents submission | ✅ Pass |
| TC-M27 | Admin tries to self-remove | Admin clicks remove on themselves | Error: "Admins cannot remove themselves" | Error notification shown | ✅ Pass |

---

## 3. Expense Management Test Cases

### Functional Testing

| Test ID | Description | Input | Expected Output | Observed Output | Status |
|---------|-------------|-------|-----------------|-----------------|--------|
| TC-M28 | Add equal split expense | Amount: 3000, Paid by: Ali, Split: Equal, 3 members | Each member's share = 1000 | Expense card shows 1000 for each | ✅ Pass |
| TC-M29 | Add exact split expense | Amount: 5000, Paid by: Ali, Split: Exact, Ali: 2000, Sara: 1500, Ahmed: 1500 | Shares match exact amounts | Expense card shows specified amounts | ✅ Pass |
| TC-M30 | Add percentage split expense | Amount: 10000, Paid by: Sara, Split: 50/30/20 | Ali: 5000, Sara: 3000, Ahmed: 2000 | Expense card shows calculated percentages | ✅ Pass |
| TC-M31 | Exact split — amounts don't match | Amount: 5000, Exact: 1000+1000+1000 = 3000 | Error: "amounts don't match total" | Error notification shown | ✅ Pass |
| TC-M32 | Percentage split — not summing to 100 | Percentages: 50 + 30 = 80% | Error: "must sum to 100%" | Error notification shown | ✅ Pass |
| TC-M33 | No group selected | Try adding expense without selecting group | Message: "Select a group" shown | Prompt displayed instead of form | ✅ Pass |

### Boundary Testing

| Test ID | Description | Input | Expected Output | Observed Output | Status |
|---------|-------------|-------|-----------------|-----------------|--------|
| TC-M34 | Zero amount expense | Amount: 0 | Error: "Amount must be greater than zero" | Error notification shown | ✅ Pass |
| TC-M35 | Negative amount expense | Amount: -500 | Error: "Amount must be greater than zero" | Error notification shown | ✅ Pass |
| TC-M36 | Very small amount (0.01) | Amount: 0.01, Equal split, 2 members | Each share = 0.01 or 0.00 (rounding) | Shares calculated with rounding | ✅ Pass |
| TC-M37 | Equal split — indivisible amount (100÷3) | Amount: 100, 3 members | Shares: 33.34, 33.33, 33.33 (total = 100) | Rounding distributed correctly | ✅ Pass |
| TC-M38 | Very large amount | Amount: 999999999 | Expense created and displayed | Large number formatted with commas | ✅ Pass |

### Equivalence Partitioning

| Test ID | Description | Input Class | Expected Output | Observed Output | Status |
|---------|-------------|-------------|-----------------|-----------------|--------|
| TC-M39 | Valid expense (positive, finite) | Valid (100-100000) | Expense created | Created successfully | ✅ Pass |
| TC-M40 | Invalid expense (zero) | Invalid (boundary) | Rejected | Error shown | ✅ Pass |
| TC-M41 | Invalid expense (negative) | Invalid (< 0) | Rejected | Error shown | ✅ Pass |
| TC-M42 | Invalid expense (NaN) | Invalid (text input) | Rejected | HTML input validation | ✅ Pass |

---

## 4. Balance Calculation Test Cases

### Functional Testing

| Test ID | Description | Input | Expected Output | Observed Output | Status |
|---------|-------------|-------|-----------------|-----------------|--------|
| TC-M43 | Assignment example scenario | Ali pays 3000 dinner (equal/3), Sara pays 1500 fuel (equal/3) | Ali: +1500, Sara: 0, Ahmed: -1500 | Balance cards show correct positions | ✅ Pass |
| TC-M44 | Simplified debts | Same as TC-M43 | 1 transaction: Ahmed → Ali 1500 | Single simplified transaction shown | ✅ Pass |
| TC-M45 | Circular debts cancel out | A pays 2000 for A&B, B pays 2000 for B&C, C pays 2000 for A&C | All balances = 0, no transactions needed | All cards show "Settled ✓" | ✅ Pass |
| TC-M46 | Single expense — only payer and others | Ali pays 1000 for Ali, Sara, Ahmed | Ali: +666.67, Sara: -333.33, Ahmed: -333.33 | Correct balances displayed | ✅ Pass |
| TC-M47 | Multiple expenses same payer | Ali pays 1000 and 2000 (both equal/3) | Ali gets back 2000 total | Net balance shows +2000 for Ali | ✅ Pass |

### Boundary Testing

| Test ID | Description | Input | Expected Output | Observed Output | Status |
|---------|-------------|-------|-----------------|-----------------|--------|
| TC-M48 | No expenses in group | Select group with 0 expenses | "No balances to show" message | Empty state message displayed | ✅ Pass |
| TC-M49 | Single person group expense | 1 member, add expense | Payer owes themselves (net 0) | Balance shows 0 | ✅ Pass |

---

## 5. Settlement Test Cases

### Functional Testing

| Test ID | Description | Input | Expected Output | Observed Output | Status |
|---------|-------------|-------|-----------------|-----------------|--------|
| TC-M50 | Record full settlement | Ahmed pays Ali 1500 (full debt) | Ahmed and Ali balances go to 0 | Balance cards update to "Settled ✓" | ✅ Pass |
| TC-M51 | Record partial settlement | Ahmed pays Ali 500 (partial) | Ahmed: -1000, Ali: +1000 | Balances updated proportionally | ✅ Pass |
| TC-M52 | Quick settle from suggestion | Click "Settle" on a suggestion | Settlement recorded, balances update | Settlement appears in history, balances refresh | ✅ Pass |
| TC-M53 | Settlement history tracking | Record 3 settlements | All 3 appear in history with date/note | History section lists all settlements | ✅ Pass |

### Boundary Testing

| Test ID | Description | Input | Expected Output | Observed Output | Status |
|---------|-------------|-------|-----------------|-----------------|--------|
| TC-M54 | Self-settlement | From: Ali, To: Ali, Amount: 100 | Error: "Cannot settle with yourself" | Error notification shown | ✅ Pass |
| TC-M55 | Zero settlement amount | Amount: 0 | Error: "Amount must be greater than zero" | Error notification shown | ✅ Pass |
| TC-M56 | Negative settlement amount | Amount: -100 | Error: "Amount must be greater than zero" | Error notification shown | ✅ Pass |

---

## Test Summary

| Module | Total Tests | Functional | Boundary | Equiv. Partitioning |
|--------|-------------|------------|----------|---------------------|
| User Management | 17 | 7 | 6 | 4 |
| Group Management | 10 | 7 | 3 | - |
| Expense Management | 15 | 6 | 5 | 4 |
| Balance Calculation | 7 | 5 | 2 | - |
| Settlement | 7 | 4 | 3 | - |
| **Total** | **56** | **29** | **19** | **8** |

> All 56 manual test cases cover functional testing, boundary testing, and equivalence partitioning across all 5 modules of the system.
