// import React, { useState } from 'react';

// const DateInput = () => {
//   const [selectedDate, setSelectedDate] = useState('');
//   const [readingPlan, setReadingPlan] = useState('');
//   const [text, setText] = useState('');

//   const handleChange = (event) => {
//     const newDate = event.target.value;
//     setSelectedDate(newDate);
//     fetchReading(newDate)
     
//   };

//   const fetchReading = async (selectedDate) => {
//     console.log(selectedDate)
//     try {
//         const response = await fetch(`http://127.0.0.1:8000/readings/${selectedDate}/`);
//         const data = await response.json();

//         if (response.ok) {
//             setReadingPlan(data); 
//             // console.log(data)
//         } else {
//             console.error("Error:", data.error);
//         }
//     } catch (error) {
//         console.error("Error fetching reading:", error);
//     }
// };

//   const fetchText = async () => {

//     try {
//       const response = await fetch(`http://127.0.0.1:8000/text/`);
//       // const response = await fetch(`http://127.0.0.1:8000/text/${readingPlan.old_testament}/`);
//       const data = await response.json();
//       console.log(data.readings[0])

//       if (response.ok) {
//           setText(data);
//       } else {
//         console.error("Error:", data.error);
//       }
//     } catch (error) {
//       console.error("Error fetching reading:", error);
//     }
//   }

// return (
//     <div>
//       <h2>Select a date:</h2>
//       <input type="date" value={selectedDate} onChange={handleChange} />
      
//       {readingPlan && (
//         <div>
//           <h3>Reading Plan for {readingPlan.date}</h3>
//           <button value="buttonValue" id='myButton' onClick={fetchText}><strong>Old Testament:</strong> {readingPlan.old_testament}</button>
//           <p><strong>New Testament:</strong> {readingPlan.new_testament}</p>
//           <p><strong>Psalm:</strong> {readingPlan.psalm}</p>
//         </div>
//       )}
//     </div>
//   );
  
// };

// export default DateInput;

