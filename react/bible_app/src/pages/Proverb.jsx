import React, { useState } from 'react';
import proverb_image from "../images/proverb_image.jpg"

const Proverb = () => {
    const [proverb, setProverb] = useState('');  

    const fetchProverb = async () => {
        try {
            const response = await fetch('http://localhost:8000/proverb/');
            const data = await response.json();
    
            console.log(data.chapter)
            if (response.ok) {
                setProverb(data);
            } else {
                console.error("Error:", data.error);
            }
        } catch (error) {
            console.error("Error fetching reading:", error);
        }
    }
    
return (
    <>
        <img src={proverb_image} width={250} className='proverb_image' alt="Description" />
        <button onClick={fetchProverb} className='proverb_button'>Daily Proverb</button>
        {proverb && (
        <div>
          <h2><strong>Proverbs {proverb.chapter}</strong> </h2>
          <br />
          <p> {proverb.text}</p>
        </div>
      )}
    </>
    )
}

export default Proverb
