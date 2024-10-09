import React, { useState } from 'react';
import { Fund } from '../interfaces/Fund';
import api from '../services/api';

interface SubscriptionFormProps {
  fund: Fund;
}

const SubscriptionForm: React.FC<SubscriptionFormProps> = ({ fund }) => {
  const [amount, setAmount] = useState<number>(0);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await api.subscribeToFund(fund.id, amount);
      alert('Suscripción exitosa');
    } catch (error) {
      alert('Error en la suscripción');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="number"
        value={amount}
        onChange={(e) => setAmount(Number(e.target.value))}
        placeholder="Monto"
        className="border p-2"
      />
      <button type="submit" className="bg-blue-500 text-white p-2 rounded">
        Suscribirse
      </button>
    </form>
  );
};

export default SubscriptionForm;