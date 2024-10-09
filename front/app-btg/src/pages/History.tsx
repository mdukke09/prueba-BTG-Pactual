import React from 'react';
import TransactionHistory from '../components/TransactionHistory';

const History: React.FC = () => {
  return (
    <div>
      <h1>Historial de Transacciones</h1>
      <TransactionHistory />
    </div>
  );
};

export default History;