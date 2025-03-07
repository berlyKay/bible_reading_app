import React, { useState } from 'react';

const Proverb = () => {
    const [proverb, setProverb] = useState('');  


    const fetchProverb = async () => {
        try {
            const response = await fetch('http://localhost:8000/proverb/');
            const data = await response.json();
    
            console.log(data)
            if (response.ok) {
                console.log("Daily Proverb:", data);  // Debugging
                setProverb(data);  // Assuming you have a state variable for this
            } else {
                console.error("Error:", data.error);
            }
        } catch (error) {
            console.error("Error fetching reading:", error);
        }



    }
        // .then(response => response.json())
        // .then(data => {
        //     const verseText = `${data.reference}: ${data.content}`; // Formatting the verse text
        //     // console.log('Random verse from Proverbs:', verseText);
        //     setRandomProverb(verseText);
        // })
        // .catch(error => console.error('Error fetching verse:', error));
    // };
    
    
return (
    <>
        <button onClick={fetchProverb}>Daily Proverb</button>
        {/* {proverb && <p>{proverb}</p>} */}
        {proverb && (
        <div>
          <h3>Daily Proverb </h3>
          <p><strong>Proverbs {proverb.chapter}:</strong> {proverb.text}</p>
        </div>
      )}
    </>
    )
}

export default Proverb
