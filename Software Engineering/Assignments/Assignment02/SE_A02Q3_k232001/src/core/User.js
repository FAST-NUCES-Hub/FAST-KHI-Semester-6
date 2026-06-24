/**
 * User class - Manages user data with contact numbers and email validation.
 * Part of the User Management module.
 */
export class User {
  static #idCounter = 0;
  static #emailRegistry = new Set();

  constructor(name, email, contactNumbers = []) {
    if (!name || typeof name !== 'string' || name.trim().length === 0) {
      throw new Error('User name is required and must be a non-empty string.');
    }

    const trimmedEmail = email?.trim().toLowerCase();
    if (!trimmedEmail || !User.validateEmail(trimmedEmail)) {
      throw new Error('A valid email address is required.');
    }

    if (User.#emailRegistry.has(trimmedEmail)) {
      throw new Error(`Email "${trimmedEmail}" is already registered.`);
    }

    this.id = ++User.#idCounter;
    this.name = name.trim();
    this.email = trimmedEmail;
    this.contactNumbers = [];
    this.createdAt = new Date();

    User.#emailRegistry.add(trimmedEmail);

    if (Array.isArray(contactNumbers)) {
      contactNumbers.forEach((num) => this.addContactNumber(num));
    }
  }

  static validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }

  addContactNumber(number) {
    const cleaned = String(number).replace(/[\s\-()]/g, '');
    if (cleaned.length < 7 || cleaned.length > 15) {
      throw new Error(`Invalid contact number: "${number}". Must be 7-15 digits.`);
    }
    if (this.contactNumbers.includes(cleaned)) {
      throw new Error(`Contact number "${cleaned}" already exists for this user.`);
    }
    this.contactNumbers.push(cleaned);
    return this;
  }

  removeContactNumber(number) {
    const cleaned = String(number).replace(/[\s\-()]/g, '');
    const index = this.contactNumbers.indexOf(cleaned);
    if (index === -1) {
      throw new Error(`Contact number "${cleaned}" not found.`);
    }
    this.contactNumbers.splice(index, 1);
    return this;
  }

  toJSON() {
    return {
      id: this.id,
      name: this.name,
      email: this.email,
      contactNumbers: [...this.contactNumbers],
      createdAt: this.createdAt.toISOString(),
    };
  }

  static resetRegistry() {
    User.#idCounter = 0;
    User.#emailRegistry.clear();
  }

  static removeFromRegistry(email) {
    User.#emailRegistry.delete(email?.trim().toLowerCase());
  }
}
