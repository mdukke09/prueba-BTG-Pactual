import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://127.0.0.1:8000';

const USER_ID = '1';

const api = {
  subscribeToFund: async (fundId: string, amount: number) => {
    const response = await axios.post(`${API_URL}/api/transactions`, {
      user_id: USER_ID,
      fund_id: fundId,
      type: "subscription",
      amount,
    });
    return response.data;
  },
  cancelSubscription: async (fundId: string) => {
    const response = await axios.post(`${API_URL}/api/transactions`, {
      user_id: USER_ID,
      fund_id: fundId,
      type: "cancellation",
    });
    return response.data;
  },
  getTransactions: async () => {
    const response = await axios.get(`${API_URL}/api/transactions`);
    return response.data;
  },
  getFunds: async () => {
    const response = await axios.get(`${API_URL}/api/funds`);
    return response.data;
  },
  getFund: async (fundId: string) => {
    const response = await axios.get(`${API_URL}/api/funds/${fundId}`);
    return response.data;
  },
};

export default api;