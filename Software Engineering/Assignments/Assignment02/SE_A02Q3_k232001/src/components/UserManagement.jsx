import { useState } from 'react';
import { useApp } from '../store/AppStore';

const UserIcon = () => (
  <svg viewBox="0 0 24 24"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
);

export default function UserManagement() {
  const { state, createUser } = useApp();
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [contacts, setContacts] = useState('');
  const [showForm, setShowForm] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    const contactList = contacts
      .split(',')
      .map((c) => c.trim())
      .filter((c) => c.length > 0);
    const result = createUser(name, email, contactList);
    if (result) {
      setName('');
      setEmail('');
      setContacts('');
      setShowForm(false);
    }
  };

  return (
    <div className="module-card" id="user-management">
      <div className="module-header">
        <div className="module-icon"><UserIcon /></div>
        <div>
          <h2>Users</h2>
          <p className="module-subtitle">{state.users.length} registered</p>
        </div>
        <button
          className="btn btn-primary"
          onClick={() => setShowForm(!showForm)}
          id="toggle-user-form"
        >
          {showForm ? 'Cancel' : '+ New User'}
        </button>
      </div>

      {showForm && (
        <form className="form-grid slide-in" onSubmit={handleSubmit} id="create-user-form">
          <div className="form-group">
            <label htmlFor="user-name">Full Name</label>
            <input
              id="user-name"
              type="text"
              placeholder="e.g. Ali Khan"
              value={name}
              onChange={(e) => setName(e.target.value)}
              required
              className="input-field"
            />
          </div>
          <div className="form-group">
            <label htmlFor="user-email">Email Address</label>
            <input
              id="user-email"
              type="email"
              placeholder="e.g. ali@email.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              className="input-field"
            />
          </div>
          <div className="form-group full-width">
            <label htmlFor="user-contacts">Contact Numbers <span className="label-hint">(comma-separated)</span></label>
            <input
              id="user-contacts"
              type="text"
              placeholder="e.g. 03001234567, 03219876543"
              value={contacts}
              onChange={(e) => setContacts(e.target.value)}
              className="input-field"
            />
          </div>
          <button type="submit" className="btn btn-success full-width" id="submit-user">
            Create User
          </button>
        </form>
      )}

      <div className="user-grid">
        {state.users.length === 0 ? (
          <div className="empty-state">
            <span className="empty-icon">
              <svg viewBox="0 0 24 24"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><line x1="19" y1="8" x2="19" y2="14"/><line x1="22" y1="11" x2="16" y2="11"/></svg>
            </span>
            <p>No users yet. Create your first user to get started.</p>
          </div>
        ) : (
          state.users.map((user) => (
            <div key={user.id} className="user-card" id={`user-card-${user.id}`}>
              <div className="user-avatar">
                {user.name.charAt(0).toUpperCase()}
              </div>
              <div className="user-info">
                <h3>{user.name}</h3>
                <p className="user-email">{user.email}</p>
                {user.contactNumbers.length > 0 && (
                  <div className="user-contacts">
                    {user.contactNumbers.map((num, i) => (
                      <span key={i} className="contact-badge">{num}</span>
                    ))}
                  </div>
                )}
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
}
