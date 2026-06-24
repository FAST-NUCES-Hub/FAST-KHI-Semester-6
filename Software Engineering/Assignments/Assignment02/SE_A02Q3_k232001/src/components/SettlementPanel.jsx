import { useState, useMemo } from 'react';
import { useApp } from '../store/AppStore';

const HandshakeIcon = () => (
  <svg viewBox="0 0 24 24"><path d="M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10z"/><path d="M8 12l2 2 4-4"/></svg>
);

export default function SettlementPanel() {
  const { state, recordSettlement, getSettlementSuggestions, getUserById } = useApp();
  const [showForm, setShowForm] = useState(false);
  const [fromUserId, setFromUserId] = useState('');
  const [toUserId, setToUserId] = useState('');
  const [amount, setAmount] = useState('');
  const [note, setNote] = useState('');

  const activeGroup = useMemo(
    () => state.groups.find((g) => g.id === state.activeGroupId),
    [state.groups, state.activeGroupId]
  );

  const suggestions = useMemo(() => {
    if (!activeGroup) return [];
    return getSettlementSuggestions(activeGroup.id);
  }, [activeGroup, getSettlementSuggestions]);

  const members = useMemo(
    () => (activeGroup ? activeGroup.getMemberList() : []),
    [activeGroup]
  );

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!activeGroup) return;

    const result = recordSettlement({
      fromUserId: parseInt(fromUserId),
      toUserId: parseInt(toUserId),
      amount: parseFloat(amount),
      groupId: activeGroup.id,
      note,
    });

    if (result) {
      setFromUserId('');
      setToUserId('');
      setAmount('');
      setNote('');
      setShowForm(false);
    }
  };

  const handleQuickSettle = (suggestion) => {
    recordSettlement({
      fromUserId: suggestion.from,
      toUserId: suggestion.to,
      amount: suggestion.amount,
      groupId: activeGroup.id,
      note: 'Quick settlement from suggestion',
    });
  };

  if (!activeGroup) {
    return (
      <div className="module-card" id="settlement-panel">
        <div className="module-header">
          <div className="module-icon"><HandshakeIcon /></div>
          <div>
            <h2>Settlements</h2>
            <p className="module-subtitle">Select a group to manage settlements</p>
          </div>
        </div>
        <div className="empty-state">
          <span className="empty-icon">
            <svg viewBox="0 0 24 24"><rect x="1" y="4" width="22" height="16" rx="2" ry="2"/><line x1="1" y1="10" x2="23" y2="10"/></svg>
          </span>
          <p>Select a group to record and view settlements.</p>
        </div>
      </div>
    );
  }

  return (
    <div className="module-card" id="settlement-panel">
      <div className="module-header">
        <div className="module-icon"><HandshakeIcon /></div>
        <div>
          <h2>Settlements — {activeGroup.name}</h2>
          <p className="module-subtitle">
            {activeGroup.settlements.length} recorded
          </p>
        </div>
        <button
          className="btn btn-primary"
          onClick={() => setShowForm(!showForm)}
          id="toggle-settlement-form"
        >
          {showForm ? 'Cancel' : '+ Record Payment'}
        </button>
      </div>

      {showForm && (
        <form className="form-grid slide-in" onSubmit={handleSubmit} id="create-settlement-form">
          <div className="form-group">
            <label htmlFor="settlement-from">Who is paying?</label>
            <select
              id="settlement-from"
              value={fromUserId}
              onChange={(e) => setFromUserId(e.target.value)}
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
            <label htmlFor="settlement-to">Paying to?</label>
            <select
              id="settlement-to"
              value={toUserId}
              onChange={(e) => setToUserId(e.target.value)}
              required
              className="input-field"
            >
              <option value="">Select receiver...</option>
              {members
                .filter((m) => m.id !== parseInt(fromUserId))
                .map((member) => (
                  <option key={member.id} value={member.id}>
                    {member.name}
                  </option>
                ))}
            </select>
          </div>
          <div className="form-group">
            <label htmlFor="settlement-amount">Amount (PKR)</label>
            <input
              id="settlement-amount"
              type="number"
              step="0.01"
              min="0.01"
              placeholder="e.g. 1000"
              value={amount}
              onChange={(e) => setAmount(e.target.value)}
              required
              className="input-field"
            />
          </div>
          <div className="form-group">
            <label htmlFor="settlement-note">Note (optional)</label>
            <input
              id="settlement-note"
              type="text"
              placeholder="e.g. Cash payment"
              value={note}
              onChange={(e) => setNote(e.target.value)}
              className="input-field"
            />
          </div>
          <button type="submit" className="btn btn-success full-width" id="submit-settlement">
            Record Settlement
          </button>
        </form>
      )}

      {suggestions.length > 0 && (
        <div className="balance-section">
          <h3 className="section-title">
            <span className="section-icon">
              <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>
            </span>
            Suggested Settlements
          </h3>
          <div className="suggestion-list">
            {suggestions.map((suggestion, idx) => {
              const fromUser = getUserById(suggestion.from);
              const toUser = getUserById(suggestion.to);
              return (
                <div key={idx} className="suggestion-card" id={`suggestion-${idx}`}>
                  <div className="suggestion-info">
                    <span className="suggestion-from">{fromUser?.name || 'Unknown'}</span>
                    <span className="suggestion-arrow">→</span>
                    <span className="suggestion-to">{toUser?.name || 'Unknown'}</span>
                    <span className="suggestion-amount">PKR {suggestion.amount.toLocaleString()}</span>
                  </div>
                  <button
                    className="btn btn-primary btn-sm"
                    onClick={() => handleQuickSettle(suggestion)}
                    id={`quick-settle-${idx}`}
                  >
                    Settle
                  </button>
                </div>
              );
            })}
          </div>
        </div>
      )}

      <div className="balance-section">
        <h3 className="section-title">
          <span className="section-icon">
            <svg viewBox="0 0 24 24"><polyline points="22 12 16 12 14 15 10 9 8 12 2 12"/></svg>
          </span>
          Settlement History
        </h3>
        {activeGroup.settlements.length === 0 ? (
          <div className="empty-state small">
            <p>No settlements recorded yet.</p>
          </div>
        ) : (
          <div className="settlement-history">
            {activeGroup.settlements.map((settlement) => {
              const fromUser = getUserById(settlement.fromUserId);
              const toUser = getUserById(settlement.toUserId);
              return (
                <div key={settlement.id} className="settlement-card" id={`settlement-${settlement.id}`}>
                  <div className="settlement-icon">✓</div>
                  <div className="settlement-info">
                    <p>
                      <strong>{fromUser?.name || 'Unknown'}</strong> paid{' '}
                      <strong>{toUser?.name || 'Unknown'}</strong>
                    </p>
                    {settlement.note && <span className="settlement-note">{settlement.note}</span>}
                    <span className="settlement-date">
                      {new Date(settlement.createdAt).toLocaleDateString()}
                    </span>
                  </div>
                  <div className="settlement-amount">
                    <span className="currency">PKR</span>
                    <span className="amount-value">{settlement.amount.toLocaleString()}</span>
                  </div>
                </div>
              );
            })}
          </div>
        )}
      </div>
    </div>
  );
}
