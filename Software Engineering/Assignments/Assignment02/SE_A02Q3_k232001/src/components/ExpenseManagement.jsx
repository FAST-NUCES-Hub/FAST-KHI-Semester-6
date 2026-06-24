import { useState, useMemo } from 'react';
import { useApp, SPLIT_TYPES } from '../store/AppStore';

const ExpenseIcon = () => (
  <svg viewBox="0 0 24 24"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
);

export default function ExpenseManagement() {
  const { state, addExpense, getUserById } = useApp();
  const [showForm, setShowForm] = useState(false);
  const [description, setDescription] = useState('');
  const [amount, setAmount] = useState('');
  const [paidById, setPaidById] = useState('');
  const [splitType, setSplitType] = useState(SPLIT_TYPES.EQUAL);
  const [exactAmounts, setExactAmounts] = useState({});
  const [percentages, setPercentages] = useState({});

  const activeGroup = useMemo(
    () => state.groups.find((g) => g.id === state.activeGroupId),
    [state.groups, state.activeGroupId]
  );

  const members = useMemo(
    () => (activeGroup ? activeGroup.getMemberList() : []),
    [activeGroup]
  );

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!activeGroup) return;

    let splitDetails = null;
    if (splitType === SPLIT_TYPES.EXACT) {
      splitDetails = {};
      members.forEach((m) => {
        splitDetails[m.id] = parseFloat(exactAmounts[m.id] || 0);
      });
    } else if (splitType === SPLIT_TYPES.PERCENTAGE) {
      splitDetails = {};
      members.forEach((m) => {
        splitDetails[m.id] = parseFloat(percentages[m.id] || 0);
      });
    }

    const result = addExpense({
      description,
      amount: parseFloat(amount),
      paidById: parseInt(paidById),
      splitType,
      splitDetails,
      groupId: activeGroup.id,
    });

    if (result) {
      setDescription('');
      setAmount('');
      setPaidById('');
      setSplitType(SPLIT_TYPES.EQUAL);
      setExactAmounts({});
      setPercentages({});
      setShowForm(false);
    }
  };

  if (!activeGroup) {
    return (
      <div className="module-card" id="expense-management">
        <div className="module-header">
          <div className="module-icon"><ExpenseIcon /></div>
          <div>
            <h2>Expenses</h2>
            <p className="module-subtitle">Select a group to manage expenses</p>
          </div>
        </div>
        <div className="empty-state">
          <span className="empty-icon">
            <svg viewBox="0 0 24 24"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
          </span>
          <p>Select a group to start adding expenses.</p>
        </div>
      </div>
    );
  }

  return (
    <div className="module-card" id="expense-management">
      <div className="module-header">
        <div className="module-icon"><ExpenseIcon /></div>
        <div>
          <h2>Expenses — {activeGroup.name}</h2>
          <p className="module-subtitle">{activeGroup.expenses.length} recorded</p>
        </div>
        <button
          className="btn btn-primary"
          onClick={() => setShowForm(!showForm)}
          id="toggle-expense-form"
        >
          {showForm ? 'Cancel' : '+ Add Expense'}
        </button>
      </div>

      {showForm && (
        <form className="form-grid slide-in" onSubmit={handleSubmit} id="create-expense-form">
          <div className="form-group">
            <label htmlFor="expense-description">Description</label>
            <input
              id="expense-description"
              type="text"
              placeholder="e.g. Dinner at restaurant"
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              required
              className="input-field"
            />
          </div>
          <div className="form-group">
            <label htmlFor="expense-amount">Amount (PKR)</label>
            <input
              id="expense-amount"
              type="number"
              step="0.01"
              min="0.01"
              placeholder="e.g. 3000"
              value={amount}
              onChange={(e) => setAmount(e.target.value)}
              required
              className="input-field"
            />
          </div>
          <div className="form-group">
            <label htmlFor="expense-paid-by">Paid By</label>
            <select
              id="expense-paid-by"
              value={paidById}
              onChange={(e) => setPaidById(e.target.value)}
              required
              className="input-field"
            >
              <option value="">Select payer...</option>
              {members.map((member) => (
                <option key={member.id} value={member.id}>
                  {member.name}
                </option>
              ))}
            </select>
          </div>
          <div className="form-group">
            <label htmlFor="expense-split-type">Split Type</label>
            <select
              id="expense-split-type"
              value={splitType}
              onChange={(e) => setSplitType(e.target.value)}
              className="input-field"
            >
              <option value={SPLIT_TYPES.EQUAL}>Equal Split</option>
              <option value={SPLIT_TYPES.EXACT}>Exact Amounts</option>
              <option value={SPLIT_TYPES.PERCENTAGE}>Percentage Split</option>
            </select>
          </div>

          {splitType === SPLIT_TYPES.EXACT && (
            <div className="form-group full-width split-details">
              <label>Exact Amounts for Each Member</label>
              <div className="split-inputs">
                {members.map((member) => (
                  <div key={member.id} className="split-input-row">
                    <span>{member.name}</span>
                    <input
                      type="number"
                      step="0.01"
                      min="0"
                      className="input-field input-sm"
                      placeholder="0.00"
                      value={exactAmounts[member.id] || ''}
                      onChange={(e) =>
                        setExactAmounts({ ...exactAmounts, [member.id]: e.target.value })
                      }
                    />
                  </div>
                ))}
              </div>
            </div>
          )}

          {splitType === SPLIT_TYPES.PERCENTAGE && (
            <div className="form-group full-width split-details">
              <label>Percentage for Each Member (must total 100%)</label>
              <div className="split-inputs">
                {members.map((member) => (
                  <div key={member.id} className="split-input-row">
                    <span>{member.name}</span>
                    <div className="percentage-input">
                      <input
                        type="number"
                        step="0.01"
                        min="0"
                        max="100"
                        className="input-field input-sm"
                        placeholder="0"
                        value={percentages[member.id] || ''}
                        onChange={(e) =>
                          setPercentages({ ...percentages, [member.id]: e.target.value })
                        }
                      />
                      <span className="percent-sign">%</span>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          <button type="submit" className="btn btn-success full-width" id="submit-expense">
            Add Expense
          </button>
        </form>
      )}

      <div className="expense-list">
        {activeGroup.expenses.length === 0 ? (
          <div className="empty-state">
            <span className="empty-icon">
              <svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>
            </span>
            <p>No expenses yet. Add the first expense for this group.</p>
          </div>
        ) : (
          activeGroup.expenses.map((expense) => {
            const payer = getUserById(expense.paidBy);
            return (
              <div key={expense.id} className="expense-card" id={`expense-card-${expense.id}`}>
                <div className="expense-main">
                  <div className="expense-icon-wrap">
                    {expense.splitType === 'equal' ? '=' : expense.splitType === 'exact' ? '#' : '%'}
                  </div>
                  <div className="expense-info">
                    <h4>{expense.description}</h4>
                    <p>Paid by <strong>{payer?.name || 'Unknown'}</strong></p>
                    <span className="split-type-badge">{expense.splitType} split</span>
                  </div>
                  <div className="expense-amount">
                    <span className="currency">PKR</span>
                    <span className="amount-value">{expense.amount.toLocaleString()}</span>
                  </div>
                </div>
                <div className="expense-shares">
                  {Array.from(expense.shares.entries()).map(([userId, share]) => {
                    const user = getUserById(userId);
                    return (
                      <div key={userId} className="share-item">
                        <span className="share-user">{user?.name || `User #${userId}`}</span>
                        <span className="share-amount">PKR {share.toLocaleString()}</span>
                      </div>
                    );
                  })}
                </div>
              </div>
            );
          })
        )}
      </div>
    </div>
  );
}
