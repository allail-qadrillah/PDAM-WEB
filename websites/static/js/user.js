import { initializeApp } from "https://www.gstatic.com/firebasejs/9.10.0/firebase-app.js";
const firebaseApp = initializeApp({
  apiKey: "AIzaSyDI7t2YW8sGONUfDzRPtkv1jwzZaS2nrgU",
  authDomain: "web-pdam-4834f.firebaseapp.com",
  databaseURL: "https://web-pdam-4834f-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "web-pdam-4834f",
  storageBucket: "web-pdam-4834f.appspot.com",
  messagingSenderId: "726848872555",
  appId: "1:726848872555:web:bc779c7bf934ffc699112e",
  measurementId: "G-KL147FH7S1"
});

import { getDatabase, ref, onValue } from "https://www.gstatic.com/firebasejs/9.10.0/firebase-database.js";
const db = getDatabase()
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

  if (pelanggan >= 10 && pelanggan <= 20) {
    document.getElementById('notifikasi').className = 'alert alert-warning mb-0 alert-dismissible alert-absolute fade show mt-2'
  } else if (pelanggan >= 20) {
    document.getElementById('notifikasi').className = 'alert alert-danger mb-0 alert-dismissible alert-absolute fade show mt-2'
  } else {
    document.getElementById('notifikasi').className = 'alert alert-danger mb-0 alert-dismissible alert-absolute fade mt-2'
  }
});