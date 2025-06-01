import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getFirestore } from "firebase/firestore";
import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword, signOut, onAuthStateChanged } from "firebase/auth";
const firebaseConfig = {
    apiKey: "AIzaSyDvipHYjm3xl9UTL8ski2ntlqVJF9sbrLQ",
    authDomain: "tracker-of-doing-homework.firebaseapp.com",
    projectId: "tracker-of-doing-homework",
    storageBucket: "tracker-of-doing-homework.firebasestorage.app",
    messagingSenderId: "65009329603",
    appId: "1:65009329603:web:3f3d6fd9e9b7a2c1840976",
    measurementId: "G-S1SE0JZNB2"
};

const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const db = getFirestore(app);
const auth = getAuth(app);
export { db, auth, createUserWithEmailAndPassword, signInWithEmailAndPassword, signOut, onAuthStateChanged };
