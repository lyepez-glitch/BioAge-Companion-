import React, { useState, useEffect } from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';

export default function BiologicalAgeScreen({ navigation }) {
  const [biologicalAge, setBiologicalAge] = useState(null);

  useEffect(() => {
    // Call the backend API to calculate the biological age
    // For demo purposes, we'll set a fixed value
    const token = localStorage.getItem("token");
    // You would typically send this data to your backend here
    fetch('http://localhost:8000/api/biological-age/', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json',
      }
    })
      .then(response => response.json())
      .then(data => {
        console.log('response',data)
        setBiologicalAge(data.biological_age);
      });

  }, []);

  return (
    <View style={styles.container}>
      <Text>Your Biological Age is: {biologicalAge}</Text>
      <Button title="See Recommendations" onPress={() => navigation.navigate('Recommendations')} />
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
