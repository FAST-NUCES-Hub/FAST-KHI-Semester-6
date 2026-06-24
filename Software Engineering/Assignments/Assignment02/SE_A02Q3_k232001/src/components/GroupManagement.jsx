import { useState } from 'react';
import { useApp } from '../store/AppStore';

const GroupIcon = () => (
  <svg viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
);

export default function GroupManagement() {
  const { state, createGroup, addMemberToGroup, removeMemberFromGroup, assignAdmin, dispatch } = useApp();
  const [groupName, setGroupName] = useState('');
  const [creatorId, setCreatorId] = useState('');
  const [showForm, setShowForm] = useState(false);
  const [selectedGroup, setSelectedGroup] = useState(null);
  const [addMemberId, setAddMemberId] = useState('');

  const handleCreateGroup = (e) => {
    e.preventDefault();
    const result = createGroup(groupName, parseInt(creatorId));
    if (result) {
      setGroupName('');
      setCreatorId('');
      setShowForm(false);
    }
  };

  const handleAddMember = (groupId) => {
    if (addMemberId) {
      addMemberToGroup(groupId, parseInt(addMemberId));
      setAddMemberId('');
    }
  };

  const handleSelectGroup = (groupId) => {
    setSelectedGroup(selectedGroup === groupId ? null : groupId);
    dispatch({ type: 'SET_ACTIVE_GROUP', payload: groupId });
  };

  return (
    <div className="module-card" id="group-management">
      <div className="module-header">
        <div className="module-icon"><GroupIcon /></div>
        <div>
          <h2>Groups</h2>
          <p className="module-subtitle">{state.groups.length} created</p>
        </div>
        <button
          className="btn btn-primary"
          onClick={() => setShowForm(!showForm)}
          id="toggle-group-form"
          disabled={state.users.length === 0}
        >
          {showForm ? 'Cancel' : '+ New Group'}
        </button>
      </div>

      {state.users.length === 0 && (
        <div className="warning-banner">
          Create at least one user before creating groups.
        </div>
      )}

      {showForm && (
        <form className="form-grid slide-in" onSubmit={handleCreateGroup} id="create-group-form">
          <div className="form-group">
            <label htmlFor="group-name">Group Name</label>
            <input
              id="group-name"
              type="text"
              placeholder="e.g. Weekend Trip"
              value={groupName}
              onChange={(e) => setGroupName(e.target.value)}
              required
              className="input-field"
            />
          </div>
          <div className="form-group">
            <label htmlFor="group-creator">Creator (Admin)</label>
            <select
              id="group-creator"
              value={creatorId}
              onChange={(e) => setCreatorId(e.target.value)}
              required
              className="input-field"
            >
              <option value="">Select creator...</option>
              {state.users.map((user) => (
                <option key={user.id} value={user.id}>
                  {user.name} ({user.email})
                </option>
              ))}
            </select>
          </div>
          <button type="submit" className="btn btn-success full-width" id="submit-group">
            Create Group
          </button>
        </form>
      )}

      <div className="group-list">
        {state.groups.length === 0 ? (
          <div className="empty-state">
            <span className="empty-icon">
              <svg viewBox="0 0 24 24"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg>
            </span>
            <p>No groups yet. Create a group to start splitting expenses.</p>
          </div>
        ) : (
          state.groups.map((group) => (
            <div
              key={group.id}
              className={`group-card ${selectedGroup === group.id ? 'expanded' : ''} ${
                state.activeGroupId === group.id ? 'active-group' : ''
              }`}
              id={`group-card-${group.id}`}
            >
              <div
                className="group-card-header"
                onClick={() => handleSelectGroup(group.id)}
              >
                <div className="group-name-section">
                  <h3>{group.name}</h3>
                  <span className="member-count">{group.getMemberCount()} members</span>
                </div>
                <div className="group-stats">
                  <span className="stat-badge">{group.expenses.length} expenses</span>
                  <span className="expand-icon">{selectedGroup === group.id ? '−' : '+'}</span>
                </div>
              </div>

              {selectedGroup === group.id && (
                <div className="group-details slide-in">
                  <div className="member-list">
                    <h4>Members</h4>
                    {group.getMemberList().map((member) => (
                      <div key={member.id} className="member-item">
                        <span className="member-name">
                          {member.name}
                          {group.isAdmin(member.id) && (
                            <span className="admin-badge">Admin</span>
                          )}
                        </span>
                        <div className="member-actions">
                          {!group.isAdmin(member.id) && (
                            <>
                              <button
                                className="btn-icon"
                                title="Make Admin"
                                onClick={() => {
                                  const adminId = Array.from(group.admins)[0];
                                  assignAdmin(group.id, member.id, adminId);
                                }}
                              >
                                A
                              </button>
                              <button
                                className="btn-icon btn-danger-icon"
                                title="Remove"
                                onClick={() => {
                                  const adminId = Array.from(group.admins)[0];
                                  removeMemberFromGroup(group.id, member.id, adminId);
                                }}
                              >
                                ×
                              </button>
                            </>
                          )}
                        </div>
                      </div>
                    ))}
                  </div>

                  <div className="add-member-section">
                    <select
                      className="input-field"
                      value={addMemberId}
                      onChange={(e) => setAddMemberId(e.target.value)}
                      id={`add-member-select-${group.id}`}
                    >
                      <option value="">Add a member...</option>
                      {state.users
                        .filter((u) => !group.isMember(u.id))
                        .map((user) => (
                          <option key={user.id} value={user.id}>
                            {user.name}
                          </option>
                        ))}
                    </select>
                    <button
                      className="btn btn-primary btn-sm"
                      onClick={() => handleAddMember(group.id)}
                      disabled={!addMemberId}
                      id={`add-member-btn-${group.id}`}
                    >
                      Add
                    </button>
                  </div>
                </div>
              )}
            </div>
          ))
        )}
      </div>
    </div>
  );
}
