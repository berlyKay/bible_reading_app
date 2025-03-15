import React, { useState } from 'react';

const Plan = () => {
  const [selectedDate, setSelectedDate] = useState('');
  const [readings, setReadings] = useState([]);
  const [chapterText, setChapterText] = useState('');
  
  const handleChange = async (event) => {
    const newDate = event.target.value;
    setSelectedDate(newDate);

    try {
      const response = await fetch(`http://127.0.0.1:8000/readings/${newDate}/`)
      if (!response.ok) {
        throw new Error("Failed to fetch data");
      }
      const data = await response.json();
      setReadings(data.readings);
    } catch (error) {
      console.log("Error fetching readings:", error);
    }
  };

  const handleChapterClick = async (book, chapter) => {
    try {
      const response = await fetch(`http://127.0.0.1:8000/readings/${book}/${chapter}/`)
      if (!response.ok) {
        throw new Error("Failed to fetch data");
      }
      const data = await response.json();
      setChapterText(data.text);
    } catch (error) {
      console.log("Error fetching readings:", error);
    }
  }

  


  return (
    <div>
      <h1>Reading Plan</h1>
      <input type="date" onChange={handleChange} value={selectedDate} />
      <ul>
        {readings.map((reading, index) => (
          <li 
            key={index} 
            onClick={() => handleChapterClick(reading.book, reading.chapter)} 
            style={{ cursor: "pointer" }}
            >
            {reading.book} {reading.chapter}
            {/* {readings} */}
          </li>
        ))}
      </ul>
      {chapterText && (
        <div>
          <h2>Chapter Text</h2>
          <p>{chapterText}</p>
        </div>
      )}
    </div>
  )
}

export default Plan;

