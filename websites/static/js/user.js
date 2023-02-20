import { initializeApp } from "https://www.gstatic.com/firebasejs/9.10.0/firebase-app.js";
const firebaseApp = initializeApp({
  authDomain: "web-pdam.firebaseapp.com",
  databaseURL: "https://web-pdam-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "web-pdam",
  storageBucket: "web-pdam.appspot.com",
  messagingSenderId: "264007938304",
  appId: "1:264007938304:web:d2170dfa7c25cb930943e5"
});

import { getDatabase, ref, onValue } from "https://www.gstatic.com/firebasejs/9.10.0/firebase-database.js";
const db  = getDatabase()
const golongan = document.getElementById('golongan').innerHTML

function count_pembayaran(golongan, volume_air) {
  if (golongan === "Rumah Tangga A") {
    if (volume_air >= 0 && volume_air <= 10) {
      return volume_air * 2.5 + 4.5 + 3;
    } else {
      return volume_air * 3.5 + 4.5 + 3;
    }
  } else if (golongan === "Rumah Tangga B") {
    if (volume_air >= 0 && volume_air <= 10) {
      return volume_air * 3 + 4.5 + 3;
    } else {
      return volume_air * 3.85 + 4.5 + 3;
    }
  } else if (golongan === "Rumah Tangga C") {
    if (volume_air >= 0 && volume_air <= 10) {
      return volume_air * 3.25 + 4.5 + 3;
    } else {
      return volume_air * 4.2 + 4.5 + 3;
    }
  } else if (golongan === "Rumah Tangga D") {
    if (volume_air >= 0 && volume_air <= 10) {
      return volume_air * 3.5 + 4.5 + 3;
    } else {
      return volume_air * 4.55 + 4.5 + 3;
    }
  } else if (golongan === "Niaga Kecil") {
    if (volume_air >= 0 && volume_air <= 10) {
      return volume_air * 3.5 + 4.5 + 3;
    } else {
      return volume_air * 6.3 + 4.5 + 3;
    }
  } else if (golongan === "Niaga Menengah") {
    if (volume_air >= 0 && volume_air <= 10) {
      return volume_air * 3.85 + 4.5 + 3;
    } else {
      return volume_air * 6.65 + 4.5 + 3;
    }
  } else if (golongan === "Niaga Besar") {
    if (volume_air >= 0 && volume_air <= 10) {
      return volume_air * 4.2 + 4.5 + 3;
    } else {
      return volume_air * 7 + 4.5 + 3;
    }
  }
}

// update data
onValue(ref(db, '/'), (snapshot) => {
  const data = snapshot.val();
  var pelanggan = data.pelanggan
  document.getElementById('debit-pelanggan').innerHTML = `${pelanggan} m<sup>3</sup>`
  document.getElementById('total-pembayaran').innerHTML = `Rp${count_pembayaran(golongan, pelanggan).toFixed(3)}`
  // console.log()
});