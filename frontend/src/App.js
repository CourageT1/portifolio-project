import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [barcode, setBarcode] = useState('');
  const [productInfo, setProductInfo] = useState(null);

  const getProductInfo = async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:5000/product/${barcode}`);
      setProductInfo(response.data);
    } catch (error) {
      console.error('Error retrieving product information:', error);
    }
  };

  return (
    <div>
      <h1>Barcode Scanner App</h1>
      <input
        type="text"
        placeholder="Enter barcode"
        value={barcode}
        onChange={(e) => setBarcode(e.target.value)}
      />
      <button onClick={getProductInfo}>Get Product Info</button>

      {productInfo && (
        <div>
          <h2>Product Information:</h2>
          <p>Price: ${productInfo.price}</p>
          <p>Expiry Date: {productInfo.expiry_date}</p>
          <p>Promotion: {productInfo.promotion}</p>
        </div>
      )}
    </div>
  );
}

export default App;
