export interface User {
    _id: string;
    name: string;
    email: string;
    phone: string;
    balance: number;
    funds: Array<{
      fund_id: string;
      amount: number;
      date_subscribed: string;
    }>;
  }  