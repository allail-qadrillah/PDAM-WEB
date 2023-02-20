import { initializeApp } from "https://www.gstatic.com/firebasejs/9.10.0/firebase-app.js";
const firebaseApp = initializeApp({
  authDomain: "web-pdam.firebaseapp.com",
  databaseURL: "https://web-pdam-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "web-pdam",
  storageBucket: "web-pdam.appspot.com",
  messagingSenderId: "264007938304",
  appId: "1:264007938304:web:d2170dfa7c25cb930943e5"
});

import { getDatabase, ref, onValue, get, update } from "https://www.gstatic.com/firebasejs/9.10.0/firebase-database.js";
const db = getDatabase()
// update data
onValue(ref(db, '/'), (snapshot) => {
  const data = snapshot.val();
  document.getElementById('debit-pelanggan').innerHTML = data.pelanggan 
});