// // import { useState, useEffect } from "react";

// // export default function playAudio({ apiUrl }) {
// //     const [audioSrc, setAudioSrc] = useState("");

// //     useEffect(() => {
// //         fetch('http://localhost:8000/audio/')
// //             .then((response) => response.json())
// //             .then((data) => {
// //                 if (data.fileName) {
// //                     console.log(data.fileName)
// //                     setAudioSrc(data.fileName);
// //                 }
// //             })
// //             .catch((error) => console.error("Error fetching audio:", error));
// //     }, [apiUrl])

// //     return (
// //         <div>
// //             <button onClick={playAudio}>Play audio</button>
// //             {audioSrc ? (
// //                 <audio controls>
// //                     <source src={audioSrc} type="audio/mpeg" />
// //                     Your browser does not support the audio element.
// //                 </audio>
// //             ) : (
// //                 <p>Loading audio...</p>
// //             )}
// //         </div>
// //     )
// // }


// import { useState, useEffect } from "react";

// export default function PlayAudio() {
//   const [audioSrc, setAudioSrc] = useState("");

//   useEffect(() => {
//     fetch("http://127.0.0.1:8000/audio/") // Ensure this is correct
//       .then(response => response.json())
//       .then(data => {
//         setAudioSrc(data.fileName);
//       })
//       .catch(error => console.error("Error fetching audio:", error));
//   }, []);
// //   useEffect(() => {
// //     fetch("http://127.0.0.1:8000/audio/") // Ensure this is correct
// //       .then(response => response.json())
// //       .then(data => {
// //         setAudioSrc(data.fileName);
// //       })
// //       .catch(error => console.error("Error fetching audio:", error));
// //   }, []);

//   return (
//     <div>
//       {audioSrc ? (
//         <>
//           <p>Now Playing: {audioSrc}</p>
//           <audio controls>
//             <source src={audioSrc} type="audio/mpeg" />
//             Your browser does not support the audio element.
//           </audio>
//         </>
//       ) : (
//         <p>Loading audio...</p>
//       )}
//     </div>
//   );
// }
