import { useMemo } from 'react';
import { useApp } from '../store/AppStore';

const ChartIcon = () => (
  <svg viewBox="0 0 24 24"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>
);

export default function BalanceDashboard() {
  const { state, getGroupBalances, getUserById } = useApp();

  const activeGroup = useMemo(
    () => state.groups.find((g) => g.id === state.activeGroupId),
    [state.groups, state.activeGroupId]
  );

  const balances = useMemo(() => {
    if (!activeGroup) return null;
    return getGroupBalances(activeGroup.id);
  }, [activeGroup, getGroupBalances]);

  if (!activeGroup || !balances) {
    return (
      <div className="module-card" id="balance-dashboard">
        <div className="module-header">
          <div className="module-icon"><ChartIcon /></div>
          <div>
            <h2>Balances</h2>
            <p className="module-subtitle">Select a group to view balances</p>
          </div>
        </div>
        <div className="empty-state">
          <span className="empty-icon">
            <svg viewBox="0 0 24 24"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>
          </span>
          <p>Select a group to see balance calculations.</p>
        </div>
      </div>
    );
  }

  const netBalanceEntries = Array.from(balances.netBalances.entries()).sort(
    (a, b) => b[1] - a[1]
  );

  return (
    <div className="module-card" id="balance-dashboard">
      <div className="module-header">
        <div className="module-icon"><ChartIcon /></div>
        <div>
          <h2>Balances — {activeGroup.name}</h2>
          <p className="module-subtitle">Real-time calculations</p>
        </div>
      </div>

      <div className="balance-section">
        <h3 className="section-title">
          <span className="section-icon">
            <svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="16"/><line x1="8" y1="12" x2="16" y2="12"/></svg>
          </span>
          Net Balances
        </h3>
        <div className="balance-grid">
          {netBalanceEntries.length === 0 ? (
            <div className="empty-state small">
              <p>No balances to show. Add some expenses first.</p>
            </div>
          ) : (
            netBalanceEntries.map(([userId, balance]) => {
              const user = getUserById(userId);
              const isPositive = balance > 0;
              const isZero = Math.abs(balance) < 0.01;
              return (
                <div
                  key={userId}
                  className={`balance-card ${isZero ? 'balanced' : isPositive ? 'positive' : 'negative'}`}
                  id={`balance-card-${userId}`}
                >
                  <div className="balance-avatar">
                    {user?.name?.charAt(0)?.toUpperCase() || '?'}
                  </div>
                  <div className="balance-info">
                    <h4>{user?.name || `User #${userId}`}</h4>
                    <span className={`balance-amount ${isZero ? '' : isPositive ? 'text-green' : 'text-red'}`}>
                      {isZero
                        ? 'Settled'
                        : isPositive
                        ? `Gets back PKR ${balance.toLocaleString()}`
                        : `Owes PKR ${Math.abs(balance).toLocaleString()}`}
                    </span>
                  </div>
                  <div className={`balance-indicator ${isZero ? 'ind-neutral' : isPositive ? 'ind-positive' : 'ind-negative'}`}>
                    {isZero ? '—' : isPositive ? '+' : '−'}
                  </div>
                </div>
              );
            })
          )}
        </div>
      </div>

      {balances.simplified.length > 0 && (
        <div className="balance-section">
          <h3 className="section-title">
            <span className="section-icon">
              <svg viewBox="0 0 24 24"><polyline points="13 17 18 12 13 7"/><polyline points="6 17 11 12 6 7"/></svg>
            </span>
            Simplified Settlements
            <span className="section-hint">Minimum transactions needed</span>
          </h3>
          <div className="transaction-list">
            {balances.simplified.map((txn, idx) => {
              const fromUser = getUserById(txn.from);
              const toUser = getUserById(txn.to);
              return (
                <div key={idx} className="transaction-card" id={`simplified-txn-${idx}`}>
                  <div className="txn-from">
                    <div className="txn-avatar negative-bg">
                      {fromUser?.name?.charAt(0)?.toUpperCase() || '?'}
                    </div>
                    <span>{fromUser?.name || `User #${txn.from}`}</span>
                  </div>
                  <div className="txn-arrow">
                    <span className="arrow-line"></span>
                    <span className="txn-amount">PKR {txn.amount.toLocaleString()}</span>
                    <span className="arrow-head">→</span>
                  </div>
                  <div className="txn-to">
                    <div className="txn-avatar positive-bg">
                      {toUser?.name?.charAt(0)?.toUpperCase() || '?'}
                    </div>
                    <span>{toUser?.name || `User #${txn.to}`}</span>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      )}
    </div>
  );
}
