import React from 'react';
import { useParams } from 'react-router-dom';
import SubscriptionForm from '../components/SubscriptionForm';
import { Fund } from '../interfaces/Fund';
import api from '../services/api';

const Subscribe: React.FC = () => {
  const { fundId } = useParams<{ fundId: string | undefined }>();
  const [fund, setFund] = React.useState<Fund | null>(null);

  React.useEffect(() => {
    if (fundId) {
      const fetchFund = async () => {
        try {
          const data = await api.getFund(fundId);
          setFund(data);
        } catch (error) {
          console.error('Error fetching fund:', error);
        }
      };
      fetchFund();
    }
  }, [fundId]);

  if (!fund) return <div>Cargando...</div>;

  return (
    <div>
      <h1>Suscribirse al fondo {fund.name}</h1>
      <SubscriptionForm fund={fund} />
    </div>
  );
};

export default Subscribe;