import React, { useState, useEffect } from "react";
import "./App.css";



// import React, { useState } from 'react';

// const LoginForm = () => {
//   const [username, setUsername] = useState('');
//   const [password, setPassword] = useState('');

//   const handleSubmit = (e) => {
//     e.preventDefault();


//     console.log('Username:', username);
//     console.log('Password:', password);

//     setUsername('');
//     setPassword('');
//   };

//   return (
//     <form onSubmit={handleSubmit}>
//       <div>
//         <label htmlFor="username">Username:</label>
//         <input
//           type="text"
//           id="username"
//           value={username}
//           onChange={(e) => setUsername(e.target.value)}
//         />
//       </div>
//       <div>
//         <label htmlFor="password">Password:</label>
//         <input
//           type="password"
//           id="password"
//           value={password}
//           onChange={(e) => setPassword(e.target.value)}
//         />
//       </div>
//       <button type="submit">Login</button>
//     </form>
//   );
// };

// export default LoginForm;

function App() {
  const [data, setdata] = useState({
    email: "",
    id: "",
    name: ""
  
  });

  const fetchData = () => {
    fetch("/inicio")
      .then((res) => res.json())
      .then((data) => {
        setdata({
          email: data.email,
          id: data.id,
          name: data.name
        });
      });
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div className="App">
      <h1>React and Flask</h1>
      <p>ID: {data.id}</p>
      <p>Name: {data.name}</p>
      <p>Email: {data.email}</p>
      {/* <button onClick={fetchData}>Refresh Content</button> */}
    </div>
  );

}

export default App;
