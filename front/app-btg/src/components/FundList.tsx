import React from 'react';
import { Fund } from '../interfaces/Fund';
import FundItem from './FundItem';

interface FundListProps {
  funds: Fund[];
}

const FundList: React.FC<FundListProps> = ({ funds }) => {
  return (
    <div>
      {funds.map(fund => (
        <FundItem key={fund.id} fund={fund} />
      ))}
    </div>
  );
};

export default FundList;