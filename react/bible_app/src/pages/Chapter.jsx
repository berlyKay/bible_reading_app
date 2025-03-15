import React, { useState } from 'react';


const Chapter = () => {
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
    <h3>Book Chapter</h3>
    <p>Chapter text</p>
    </>
    )
}

export default Chapter