import React from 'react';
import { useParams } from 'react-router-dom';
import { Fund } from '../interfaces/Fund';
import api from '../services/api'; // Asegúrate de importar tu archivo api

const Cancel: React.FC = () => {
  const { fundId } = useParams<{ fundId: string }>();
  const [fund, setFund] = React.useState<Fund | undefined>(undefined);

  React.useEffect(() => {
    // Fetch fund details from API
    if (fundId) {
      const fetchFund = async () => {
        const data = await api.getFund(fundId);
        setFund(data);
      };
      fetchFund();
    }
  }, [fundId]);

  const handleCancel = async () => {
    if (fundId) {
      try {
        await api.cancelSubscription(fundId);
        alert('Cancelación exitosa');
      } catch (error) {
        alert('Error en la cancelación');
      }
    }
  };

  if (!fund) return <div>Cargando...</div>;

  return (
    <div>
      <h1>Cancelar suscripción al fondo {fund.name}</h1>
      <button onClick={handleCancel} className='bg-red-500 text-white p-2 rounded'>
        Cancelar
      </button>
    </div>
  );
};

export default Cancel;
