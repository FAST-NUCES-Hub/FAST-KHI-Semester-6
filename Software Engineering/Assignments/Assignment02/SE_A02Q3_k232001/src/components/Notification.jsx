import { useApp } from '../store/AppStore';

export default function Notification() {
  const { state } = useApp();

  if (!state.notification) return null;

  return (
    <div className={`notification ${state.notification.type}`} id="notification">
      <span className="notification-icon">
        {state.notification.type === 'success' ? (
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
        ) : (
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><circle cx="12" cy="12" r="10"/><line x1="15" y1="9" x2="9" y2="15"/><line x1="9" y1="9" x2="15" y2="15"/></svg>
        )}
      </span>
      <span className="notification-message">{state.notification.message}</span>
    </div>
  );
}
