import React, { useEffect, useState } from 'react';
import { Transaction } from '../interfaces/Transaction';
import api from '../services/api';

const TransactionHistory: React.FC = () => {
  const [transactions, setTransactions] = useState<Transaction[]>([]);

  useEffect(() => {
    const fetchTransactions = async () => {
      const data = await api.getTransactions();
      setTransactions(data);
    };
    fetchTransactions();
  }, []);

  return (
    <div>
      {transactions.map(transaction => (
        <div key={transaction._id} className="p-4 border rounded">
          <p>Tipo: {transaction.type}</p>
          <p>Monto: {transaction.amount}</p>
          <p>Fecha: {new Date(transaction.date).toLocaleString()}</p>
        </div>
      ))}
    </div>
  );
};

export default TransactionHistory;