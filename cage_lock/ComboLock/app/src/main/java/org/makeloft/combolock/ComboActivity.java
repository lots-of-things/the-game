package org.makeloft.combolock;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.NumberPicker;
import android.widget.TextView;

public class ComboActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_combo);

        final TextView solution = findViewById(R.id.solution);

        final NumberPicker np1 = findViewById(R.id.numberPicker1);
        np1.setMinValue(0);
        np1.setMaxValue(9);
        final NumberPicker np2 = findViewById(R.id.numberPicker2);
        np2.setMinValue(0);
        np2.setMaxValue(9);
        final NumberPicker np3 = findViewById(R.id.numberPicker3);
        np3.setMinValue(0);
        np3.setMaxValue(9);

        NumberPicker.OnValueChangeListener onValueChangeListener =
                new 	NumberPicker.OnValueChangeListener(){
                    @Override
                    public void onValueChange(NumberPicker numberPicker, int i, int i1) {
                        if (np1.getValue()==4 && np2.getValue()==3 && np3.getValue()==3){
                            solution.setText("Notes on humans:\n\nJohn Cage was noted for his development of 'happenings' or experiential artwork. In addition to increasing audience participation, his work frequently relied on chance to determine the outcome.  He heavily utilized the hexagrams of King Wen's I Ching in his compositions.  \n\nI've almost cracked the Color team's code. The last phase will be to break into the #crs slack channel and to connect to the TV in their Scrum area.");
                        }
                    }
                };
        np1.setOnValueChangedListener(onValueChangeListener);
        np2.setOnValueChangedListener(onValueChangeListener);
        np3.setOnValueChangedListener(onValueChangeListener);

    }

}
