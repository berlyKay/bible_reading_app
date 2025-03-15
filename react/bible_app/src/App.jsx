import { Route, Routes} from "react-router-dom"
import './styles.css'
import Navbar from './components/Navbar'
import Home from './pages/Home'
import Plan from './pages/Plan'
import Chapter from './pages/Chapter'
import Account from './pages/Account'
import Proverb from "./pages/Proverb"
import { UserProvider } from "./Context/UserContext"
import CopyrightPage from "./pages/CopyrightPage"

function App() {

  return (
    <UserProvider>
    <div className='App'>
      <Navbar />
        <Routes>
          <Route path="/" element={<Home />} /> {/* Matches "/" */}
          <Route path="home" element={<Home />}></Route>
          <Route path="plan" element={<Plan />}></Route>
          <Route path="proverb" element={<Proverb />}></Route>
          <Route path="account" element={<Account />}></Route>
          <Route path="chapter" element={<Chapter />}></Route>
          <Route path="copyright" element={<CopyrightPage />}></Route>
        </Routes>
    </div>
    </UserProvider>
  );
};

export default App;



