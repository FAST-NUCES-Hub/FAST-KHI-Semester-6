import { AppProvider } from './store/AppStore';
import UserManagement from './components/UserManagement';
import GroupManagement from './components/GroupManagement';
import ExpenseManagement from './components/ExpenseManagement';
import BalanceDashboard from './components/BalanceDashboard';
import SettlementPanel from './components/SettlementPanel';
import Notification from './components/Notification';
import './index.css';

function AppContent() {
  return (
    <div className="app-container" id="app">
      <Notification />

      <header className="app-header" id="header">
        <div className="header-content">
          <div className="logo-section">
            <div className="logo-icon">S</div>
            <div>
              <h1 className="app-title">SplitEase</h1>
              <p className="app-tagline">Expense sharing made simple</p>
            </div>
          </div>
        </div>
      </header>

      <main className="main-content">
        <div className="dashboard-grid">
          <div className="col-left">
            <UserManagement />
            <GroupManagement />
          </div>
          <div className="col-right">
            <ExpenseManagement />
            <BalanceDashboard />
            <SettlementPanel />
          </div>
        </div>
      </main>
    </div>
  );
}

export default function App() {
  return (
    <AppProvider>
      <AppContent />
    </AppProvider>
  );
}
