/**
 * Group class - Manages groups with members and admin roles.
 * Part of the Group Management module.
 */
export class Group {
  static #idCounter = 0;

  constructor(name, creator) {
    if (!name || typeof name !== 'string' || name.trim().length === 0) {
      throw new Error('Group name is required and must be a non-empty string.');
    }
    if (!creator || !creator.id) {
      throw new Error('A valid creator (User) is required.');
    }

    this.id = ++Group.#idCounter;
    this.name = name.trim();
    this.members = new Map(); // userId -> User object
    this.admins = new Set(); // userId set
    this.expenses = [];
    this.settlements = [];
    this.createdAt = new Date();

    // Creator is automatically a member and admin
    this.members.set(creator.id, creator);
    this.admins.add(creator.id);
  }

  addMember(user) {
    if (!user || !user.id) {
      throw new Error('A valid User object is required.');
    }
    if (this.members.has(user.id)) {
      throw new Error(`User "${user.name}" is already a member of this group.`);
    }
    this.members.set(user.id, user);
    return this;
  }

  removeMember(userId, requesterId) {
    if (!this.members.has(userId)) {
      throw new Error('User is not a member of this group.');
    }
    if (!this.admins.has(requesterId)) {
      throw new Error('Only admins can remove members.');
    }
    if (userId === requesterId) {
      throw new Error('Admins cannot remove themselves.');
    }
    this.admins.delete(userId);
    this.members.delete(userId);
    return this;
  }

  assignAdmin(userId, requesterId) {
    if (!this.admins.has(requesterId)) {
      throw new Error('Only existing admins can assign admin roles.');
    }
    if (!this.members.has(userId)) {
      throw new Error('User must be a member of the group before becoming admin.');
    }
    this.admins.add(userId);
    return this;
  }

  removeAdmin(userId, requesterId) {
    if (!this.admins.has(requesterId)) {
      throw new Error('Only admins can remove admin roles.');
    }
    if (userId === requesterId) {
      throw new Error('Cannot remove your own admin role.');
    }
    if (!this.admins.has(userId)) {
      throw new Error('User is not an admin.');
    }
    if (this.admins.size <= 1) {
      throw new Error('Group must have at least one admin.');
    }
    this.admins.delete(userId);
    return this;
  }

  getMemberList() {
    return Array.from(this.members.values());
  }

  isMember(userId) {
    return this.members.has(userId);
  }

  isAdmin(userId) {
    return this.admins.has(userId);
  }

  getMemberCount() {
    return this.members.size;
  }

  toJSON() {
    return {
      id: this.id,
      name: this.name,
      members: Array.from(this.members.values()).map((u) => u.toJSON()),
      admins: Array.from(this.admins),
      expenseCount: this.expenses.length,
      createdAt: this.createdAt.toISOString(),
    };
  }

  static resetCounter() {
    Group.#idCounter = 0;
  }
}
