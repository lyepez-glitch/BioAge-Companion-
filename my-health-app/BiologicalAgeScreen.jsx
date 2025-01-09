import React, { useState, useEffect } from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';
import { TextInput } from 'react-native-paper';

export default function BiologicalAgeScreen({ navigation }) {
  const [biologicalAge, setBiologicalAge] = useState(null);

  useEffect(() => {
    const token = localStorage.getItem("token");
    fetch('http://localhost:8000/api/biological-age/', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json',
      }
    })
      .then(response => response.json())
      .then(data => setBiologicalAge(data.biological_age));
  }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.heading}>Your Biological Age is: {biologicalAge}</Text>
      <Button
        title="See Recommendations"
        onPress={() => navigation.navigate('Recommendations')}
        style={styles.button}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    padding: 20,
    alignItems: 'center', // Centers everything inside the container
  },
  heading: {
    fontSize: 24,
    marginBottom: 20,
    textAlign: 'center', // Ensures the text is centered
  },
  button: {
    width: '70%', // Make the button 70% of the container width
    marginTop: 20, // Adds space above the button
    marginBottom: 20, // Adds space below the button
  },
});
