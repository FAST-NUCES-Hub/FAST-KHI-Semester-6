/**
 * AppStore - Central state management using React Context.
 * Coordinates all modules: Users, Groups, Expenses, Settlements.
 */
import { createContext, useContext, useReducer, useCallback } from 'react';
import { User } from '../core/User';
import { Group } from '../core/Group';
import { Expense, SPLIT_TYPES } from '../core/Expense';
import { Settlement, SettlementManager } from '../core/Settlement';
import { BalanceEngine } from '../core/BalanceEngine';

const AppContext = createContext(null);

const initialState = {
  users: [],
  groups: [],
  activeGroupId: null,
  settlementManager: new SettlementManager(),
  notification: null,
};

function appReducer(state, action) {
  switch (action.type) {
    case 'ADD_USER':
      return { ...state, users: [...state.users, action.payload] };

    case 'REMOVE_USER':
      return {
        ...state,
        users: state.users.filter((u) => u.id !== action.payload),
      };

    case 'ADD_GROUP':
      return { ...state, groups: [...state.groups, action.payload] };

    case 'UPDATE_GROUP':
      return {
        ...state,
        groups: state.groups.map((g) =>
          g.id === action.payload.id ? action.payload : g
        ),
      };

    case 'SET_ACTIVE_GROUP':
      return { ...state, activeGroupId: action.payload };

    case 'ADD_EXPENSE': {
      const group = state.groups.find((g) => g.id === action.payload.groupId);
      if (group) {
        group.expenses.push(action.payload.expense);
      }
      return { ...state, groups: [...state.groups] };
    }

    case 'ADD_SETTLEMENT': {
      const grp = state.groups.find((g) => g.id === action.payload.groupId);
      if (grp) {
        grp.settlements.push(action.payload.settlement);
      }
      return { ...state, groups: [...state.groups] };
    }

    case 'SET_NOTIFICATION':
      return { ...state, notification: action.payload };

    case 'CLEAR_NOTIFICATION':
      return { ...state, notification: null };

    default:
      return state;
  }
}

export function AppProvider({ children }) {
  const [state, dispatch] = useReducer(appReducer, initialState);

  const notify = useCallback((message, type = 'success') => {
    dispatch({ type: 'SET_NOTIFICATION', payload: { message, type } });
    setTimeout(() => dispatch({ type: 'CLEAR_NOTIFICATION' }), 4000);
  }, []);

  const createUser = useCallback(
    (name, email, contactNumbers = []) => {
      try {
        const user = new User(name, email, contactNumbers);
        dispatch({ type: 'ADD_USER', payload: user });
        notify(`User "${user.name}" created successfully!`);
        return user;
      } catch (err) {
        notify(err.message, 'error');
        return null;
      }
    },
    [notify]
  );

  const createGroup = useCallback(
    (name, creatorId) => {
      try {
        const creator = state.users.find((u) => u.id === creatorId);
        if (!creator) throw new Error('Creator user not found.');
        const group = new Group(name, creator);
        dispatch({ type: 'ADD_GROUP', payload: group });
        notify(`Group "${group.name}" created!`);
        return group;
      } catch (err) {
        notify(err.message, 'error');
        return null;
      }
    },
    [state.users, notify]
  );

  const addMemberToGroup = useCallback(
    (groupId, userId) => {
      try {
        const group = state.groups.find((g) => g.id === groupId);
        const user = state.users.find((u) => u.id === userId);
        if (!group) throw new Error('Group not found.');
        if (!user) throw new Error('User not found.');
        group.addMember(user);
        dispatch({ type: 'UPDATE_GROUP', payload: group });
        notify(`${user.name} added to ${group.name}!`);
        return true;
      } catch (err) {
        notify(err.message, 'error');
        return false;
      }
    },
    [state.groups, state.users, notify]
  );

  const removeMemberFromGroup = useCallback(
    (groupId, userId, requesterId) => {
      try {
        const group = state.groups.find((g) => g.id === groupId);
        if (!group) throw new Error('Group not found.');
        group.removeMember(userId, requesterId);
        dispatch({ type: 'UPDATE_GROUP', payload: group });
        notify('Member removed from group.');
        return true;
      } catch (err) {
        notify(err.message, 'error');
        return false;
      }
    },
    [state.groups, notify]
  );

  const assignAdmin = useCallback(
    (groupId, userId, requesterId) => {
      try {
        const group = state.groups.find((g) => g.id === groupId);
        if (!group) throw new Error('Group not found.');
        group.assignAdmin(userId, requesterId);
        dispatch({ type: 'UPDATE_GROUP', payload: group });
        notify('Admin role assigned!');
        return true;
      } catch (err) {
        notify(err.message, 'error');
        return false;
      }
    },
    [state.groups, notify]
  );

  const addExpense = useCallback(
    ({ description, amount, paidById, splitType, splitDetails, groupId }) => {
      try {
        const group = state.groups.find((g) => g.id === groupId);
        if (!group) throw new Error('Group not found.');

        const participants = Array.from(group.members.keys());
        const expense = new Expense({
          description,
          amount: parseFloat(amount),
          paidBy: paidById,
          splitType,
          splitDetails,
          groupId,
          participants,
        });

        dispatch({
          type: 'ADD_EXPENSE',
          payload: { groupId, expense },
        });
        notify(`Expense "${description}" added!`);
        return expense;
      } catch (err) {
        notify(err.message, 'error');
        return null;
      }
    },
    [state.groups, notify]
  );

  const recordSettlement = useCallback(
    ({ fromUserId, toUserId, amount, groupId, note }) => {
      try {
        const settlement = state.settlementManager.recordSettlement({
          fromUserId,
          toUserId,
          amount: parseFloat(amount),
          groupId,
          note,
        });

        const group = state.groups.find((g) => g.id === groupId);
        if (group) {
          group.settlements.push(settlement);
          dispatch({ type: 'UPDATE_GROUP', payload: group });
        }

        notify('Settlement recorded!');
        return settlement;
      } catch (err) {
        notify(err.message, 'error');
        return null;
      }
    },
    [state.groups, state.settlementManager, notify]
  );

  const getGroupBalances = useCallback(
    (groupId) => {
      const group = state.groups.find((g) => g.id === groupId);
      if (!group) return { netBalances: new Map(), simplified: [], detailed: [] };

      const netBalances = BalanceEngine.calculateNetBalances(
        group.expenses,
        group.settlements
      );
      const simplified = BalanceEngine.simplifyDebts(
        group.expenses,
        group.settlements
      );
      const detailed = BalanceEngine.getDetailedDebts(
        group.expenses,
        group.settlements
      );

      return { netBalances, simplified, detailed };
    },
    [state.groups]
  );

  const getSettlementSuggestions = useCallback(
    (groupId) => {
      const { netBalances } = getGroupBalances(groupId);
      return state.settlementManager.suggestSettlements(netBalances);
    },
    [getGroupBalances, state.settlementManager]
  );

  const getUserById = useCallback(
    (userId) => state.users.find((u) => u.id === userId),
    [state.users]
  );

  const value = {
    state,
    dispatch,
    createUser,
    createGroup,
    addMemberToGroup,
    removeMemberFromGroup,
    assignAdmin,
    addExpense,
    recordSettlement,
    getGroupBalances,
    getSettlementSuggestions,
    getUserById,
    notify,
  };

  return <AppContext.Provider value={value}>{children}</AppContext.Provider>;
}

export function useApp() {
  const context = useContext(AppContext);
  if (!context) {
    throw new Error('useApp must be used within an AppProvider');
  }
  return context;
}

export { SPLIT_TYPES };
