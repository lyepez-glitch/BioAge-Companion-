import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet } from 'react-native';

export default function RecommendationsScreen() {
  const [recommendations, setRecommendations] = useState([]);

  useEffect(() => {
    const token = localStorage.getItem("token");
    fetch('http://localhost:8000/api/recommendations/', {
      method: 'GET',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json',
      }
    })
      .then(response => response.json())
      .then(data => {
        console.log('response',data)
        setRecommendations(data.recommendations);
      });


      // Replace with real recommendations
  }, []);

  return (
    <View style={styles.container}>
      <Text>Personalized Recommendations:</Text>
      {recommendations.map((rec, index) => (
        <Text key={index}>{rec}</Text>
      ))}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    padding: 20,
  },
});
