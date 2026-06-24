/**
 * Automated Tests — Part 3
 * 
 * Unit Tests for Group Management Module
 */
import { User } from '../core/User';
import { Group } from '../core/Group';

describe('Group Management Module', () => {
  let creator;
  let member1;
  let member2;

  beforeEach(() => {
    User.resetRegistry();
    Group.resetCounter();
    creator = new User('Ali Khan', 'ali@email.com');
    member1 = new User('Sara Ahmed', 'sara@email.com');
    member2 = new User('Ahmed Raza', 'ahmed@email.com');
  });

  // TEST 11: Create group
  test('TC-A11: should create a group with creator as member and admin', () => {
    const group = new Group('Trip Friends', creator);
    
    expect(group.name).toBe('Trip Friends');
    expect(group.isMember(creator.id)).toBe(true);
    expect(group.isAdmin(creator.id)).toBe(true);
    expect(group.getMemberCount()).toBe(1);
  });

  // TEST 12: Add members
  test('TC-A12: should add members to a group', () => {
    const group = new Group('Dinner Group', creator);
    group.addMember(member1);
    group.addMember(member2);
    
    expect(group.getMemberCount()).toBe(3);
    expect(group.isMember(member1.id)).toBe(true);
    expect(group.isMember(member2.id)).toBe(true);
  });

  // TEST 13: Prevent duplicate members
  test('TC-A13: should reject adding duplicate members', () => {
    const group = new Group('Test Group', creator);
    group.addMember(member1);
    
    expect(() => group.addMember(member1)).toThrow('already a member');
  });

  // TEST 14: Remove member (admin action)
  test('TC-A14: should allow admin to remove a member', () => {
    const group = new Group('Test Group', creator);
    group.addMember(member1);
    group.removeMember(member1.id, creator.id);
    
    expect(group.isMember(member1.id)).toBe(false);
    expect(group.getMemberCount()).toBe(1);
  });

  // TEST 15: Non-admin cannot remove
  test('TC-A15: should prevent non-admin from removing members', () => {
    const group = new Group('Test Group', creator);
    group.addMember(member1);
    
    expect(() => group.removeMember(creator.id, member1.id)).toThrow('Only admins');
  });

  // TEST 16: Assign admin role
  test('TC-A16: should assign admin role to a member', () => {
    const group = new Group('Test Group', creator);
    group.addMember(member1);
    group.assignAdmin(member1.id, creator.id);
    
    expect(group.isAdmin(member1.id)).toBe(true);
  });

  // TEST 17: Invalid group name
  test('TC-A17: should reject empty group name', () => {
    expect(() => new Group('', creator)).toThrow('name is required');
    expect(() => new Group('   ', creator)).toThrow('name is required');
  });

  // TEST 18: Admin cannot remove themselves
  test('TC-A18: should prevent admin from removing themselves', () => {
    const group = new Group('Test Group', creator);
    
    expect(() => group.removeMember(creator.id, creator.id)).toThrow('cannot remove themselves');
  });
});
