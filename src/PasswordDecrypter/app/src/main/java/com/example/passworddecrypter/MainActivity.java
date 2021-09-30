package com.example.passworddecrypter;

import androidx.appcompat.app.AppCompatActivity;

import android.content.ClipData;
import android.content.ClipboardManager;
import android.content.Context;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
    public void ClickBt1(View buttonview)
    {   String ReverseString="";
        EditText editText=findViewById(R.id.Ed1);
        TextView textView=findViewById(R.id.textView2);
        Button copy=findViewById(R.id.button2);

        String userString=editText.getText().toString();
        char[]EnterString=userString.toCharArray();
        for(int count=EnterString.length-1;count>=0;count--)
        {
            ReverseString=ReverseString+EnterString[count];

        }
        textView.setText(ReverseString);

        String finalReverseString = ReverseString;
        copy.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String value= finalReverseString;
                if(value.isEmpty()){

                    Toast.makeText(getApplicationContext(), "Please Insert Data!!!", Toast.LENGTH_SHORT).show();
                }else{
                    ClipboardManager clipboardManager = (ClipboardManager)getSystemService(Context.CLIPBOARD_SERVICE);
                    ClipData clipData = ClipData.newPlainText("Data",value);
                    clipboardManager.setPrimaryClip(clipData);
                    Toast.makeText(getApplicationContext(), "Copied To Clipboard!!!", Toast.LENGTH_SHORT).show();
                }
            }
        });

    }
}