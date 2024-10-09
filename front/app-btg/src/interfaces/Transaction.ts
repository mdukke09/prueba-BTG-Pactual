export interface Transaction {
    _id: string;
    user_id: string;
    fund_id: string;
    type: string; // "subscription" or "cancellation"
    amount: number;
    date: string;
  }