import React, { useState } from 'react';

const SimpleDatePicker = () => {
  const [selectedDate, setSelectedDate] = useState('');
  const [readingPlan, setReadingPlan] = useState('');

  const handleChange = (event) => {
    const newDate = event.target.value;
    setSelectedDate(newDate);
    console.log('Selected date:', event.target.value);
    fetchReading(newDate)
     
  };

  const fetchReading = async (selectedDate) => {
    try {
        const response = await fetch(`http://127.0.0.1:8000/reading/${selectedDate}/`);
        const data = await response.json();

        if (response.ok) {
            console.log("Reading Plan:", data);  // Debugging
            setReadingPlan(data);  // Assuming you have a state variable for this
        } else {
            console.error("Error:", data.error);
        }
    } catch (error) {
        console.error("Error fetching reading:", error);
    }
};


return (
    <div>
      <h2>Select a date:</h2>
      <input type="date" value={selectedDate} onChange={handleChange} />
      
      {readingPlan && (
        <div>
          <h3>Reading Plan for {readingPlan.date}</h3>
          <p><strong>Old Testament:</strong> {readingPlan.old_testament}</p>
          <p><strong>New Testament:</strong> {readingPlan.new_testament}</p>
          <p><strong>Psalm:</strong> {readingPlan.psalm}</p>
        </div>
      )}
    </div>
  );
  
};

export default SimpleDatePicker;

