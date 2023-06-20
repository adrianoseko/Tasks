import { useState } from 'react';

function App() {
  const [proposal, setProposal] = useState({
    full_name: '',
    cpf: '',
    address: '',
    loan_amount: 0,
  });

  const handleChange = (event) => {
    setProposal({
      ...proposal,
      [event.target.name]: event.target.value,
    });
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    const formData = new FormData();
    formData.append('full_name', proposal.full_name);
    formData.append('cpf', proposal.cpf);
    formData.append('address', proposal.address);
    formData.append('loan_amount', proposal.loan_amount);

    fetch('http://localhost:8000/api/propostas/', {
      method: 'POST',
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Full Name:
          <input type="text" name="full_name" onChange={handleChange} />
        </label>
        <label>
          CPF:
          <input type="text" name="cpf" onChange={handleChange} />
        </label>
        <label>
          Address:
          <input type="text" name="address" onChange={handleChange} />
        </label>
        <label>
          Loan Amount:
          <input type="number" name="loan_amount" onChange={handleChange} />
        </label>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default App;