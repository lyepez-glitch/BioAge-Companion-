import React, { useState } from 'react';
import { View, TextInput, Button, StyleSheet } from 'react-native';

export default function HealthMetricsScreen({ navigation }) {
  const [heartRate, setHeartRate] = useState('');
  const [sleepHours, setSleepHours] = useState('');
  const [activityLevel, setActivityLevel] = useState('');

  const handleMetricsSubmit = () => {
    // Send this data to the backend to calculate biological age, etc.
    const token = localStorage.getItem("token");
    // You would typically send this data to your backend here
    fetch('http://localhost:8000/api/health-metrics/', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        resting_heart_rate: heartRate,
        hours_of_sleep: sleepHours,
        daily_activity_level: activityLevel
      }),
    })
      .then(response => response.json())
      .then(data => {
        console.log('response',data)
      });
    navigation.navigate('BiologicalAge');
  };

  return (
    <View style={styles.container}>
      <TextInput
        style={styles.input}
        placeholder="Resting Heart Rate"
        keyboardType="numeric"
        value={heartRate}
        onChangeText={setHeartRate}
      />
      <TextInput
        style={styles.input}
        placeholder="Hours of Sleep"
        keyboardType="numeric"
        value={sleepHours}
        onChangeText={setSleepHours}
      />
      <TextInput
        style={styles.input}
        placeholder="Activity Level (1-10)"
        keyboardType="numeric"
        value={activityLevel}
        onChangeText={setActivityLevel}
      />
      <Button title="Next" onPress={handleMetricsSubmit} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    padding: 20,
  },
  input: {
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 10,
    paddingLeft: 10,
  },
});
