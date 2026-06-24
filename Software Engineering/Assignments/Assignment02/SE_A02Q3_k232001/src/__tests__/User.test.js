/**
 * Automated Tests — Part 3
 * 
 * Unit Tests for User Management Module
 * Tests: User creation, email validation, contact numbers, edge cases
 */
import { User } from '../core/User';

describe('User Management Module', () => {
  beforeEach(() => {
    User.resetRegistry();
  });

  // TEST 1: Valid user creation
  test('TC-A01: should create a user with valid name, email, and contacts', () => {
    const user = new User('Ali Khan', 'ali@email.com', ['03001234567']);
    
    expect(user.name).toBe('Ali Khan');
    expect(user.email).toBe('ali@email.com');
    expect(user.contactNumbers).toEqual(['03001234567']);
    expect(user.id).toBeGreaterThan(0);
    expect(user.createdAt).toBeInstanceOf(Date);
  });

  // TEST 2: Duplicate email validation
  test('TC-A02: should reject duplicate email addresses', () => {
    new User('Ali Khan', 'ali@email.com');
    
    expect(() => {
      new User('Ali 2', 'ali@email.com');
    }).toThrow('already registered');
  });

  // TEST 3: Invalid email format
  test('TC-A03: should reject invalid email formats', () => {
    expect(() => new User('Test', 'notanemail')).toThrow('valid email');
    expect(() => new User('Test', '')).toThrow('valid email');
    expect(() => new User('Test', '@missing.com')).toThrow('valid email');
  });

  // TEST 4: Empty/invalid name
  test('TC-A04: should reject empty or invalid names', () => {
    expect(() => new User('', 'test@email.com')).toThrow('name is required');
    expect(() => new User('   ', 'test@email.com')).toThrow('name is required');
    expect(() => new User(null, 'test@email.com')).toThrow('name is required');
  });

  // TEST 5: Multiple contact numbers
  test('TC-A05: should support multiple contact numbers per user', () => {
    const user = new User('Sara Ahmed', 'sara@email.com', [
      '03001111111',
      '03002222222',
      '03003333333',
    ]);
    
    expect(user.contactNumbers).toHaveLength(3);
    expect(user.contactNumbers).toContain('03001111111');
    expect(user.contactNumbers).toContain('03002222222');
  });

  // TEST 6: Invalid contact number (too short)
  test('TC-A06: should reject invalid contact numbers', () => {
    expect(() => {
      new User('Test User', 'test1@email.com', ['123']);
    }).toThrow('Invalid contact number');
  });

  // TEST 7: Duplicate contact number for same user
  test('TC-A07: should reject duplicate contact numbers for the same user', () => {
    const user = new User('Test User', 'test2@email.com', ['03001234567']);
    
    expect(() => {
      user.addContactNumber('03001234567');
    }).toThrow('already exists');
  });

  // TEST 8: Remove contact number
  test('TC-A08: should remove a contact number', () => {
    const user = new User('Test User', 'test3@email.com', ['03001234567', '03009876543']);
    user.removeContactNumber('03001234567');
    
    expect(user.contactNumbers).toHaveLength(1);
    expect(user.contactNumbers).not.toContain('03001234567');
  });

  // TEST 9: Serialization
  test('TC-A09: should serialize user to JSON correctly', () => {
    const user = new User('Ali', 'ali.json@test.com', ['03001234567']);
    const json = user.toJSON();
    
    expect(json).toHaveProperty('id');
    expect(json).toHaveProperty('name', 'Ali');
    expect(json).toHaveProperty('email', 'ali.json@test.com');
    expect(json.contactNumbers).toEqual(['03001234567']);
    expect(json).toHaveProperty('createdAt');
  });

  // TEST 10: Email case insensitivity
  test('TC-A10: should treat emails as case-insensitive', () => {
    new User('User One', 'UPPER@Email.COM');
    
    expect(() => {
      new User('User Two', 'upper@email.com');
    }).toThrow('already registered');
  });
});
