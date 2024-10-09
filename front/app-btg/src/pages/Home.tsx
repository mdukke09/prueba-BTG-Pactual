import React from 'react';
import FundList from '../components/FundList';
import { Fund } from '../interfaces/Fund';
import api from '../services/api';

const Home: React.FC = () => {
  const [funds, setFunds] = React.useState<Fund[]>([]);

  React.useEffect(() => {
    const fetchFunds = async () => {
      try {
        const data = await api.getFunds();
        setFunds(data);
      } catch (error) {
        console.error('Error fetching funds:', error);
      }
    };
    fetchFunds();
  }, []);

  return (
    <div>
      <h1>Bienvenido a BTG Pactual</h1>
      <FundList funds={funds} />
    </div>
  );
};

export default Home;