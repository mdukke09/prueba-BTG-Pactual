import React from 'react';
import { Fund } from '../interfaces/Fund';

interface FundItemProps {
  fund: Fund;
}

const FundItem: React.FC<FundItemProps> = ({ fund }) => {
  return (
    <div className="p-4 border rounded">
      <h2>{fund.name}</h2>
      <p>Monto mínimo: {fund.minimum_amount}</p>
      <p>Categoría: {fund.category}</p>
    </div>
  );
};

export default FundItem;