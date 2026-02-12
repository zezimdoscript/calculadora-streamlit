import streamlit as st


st.title("Calculadora Legal")


nmr1 = st.number_input("escreva seu primeiro numero :")
nmr2 = st.number_input("escreva seu segundo numero :")
resultado = 0

escuacao = st.selectbox(
 "Escolha a operação:",
 ["Soma","Subtração","Divisão","Multiplicação"]


)

if st.button("Calcular"):

 if escuacao == "Soma":
  resultado = nmr1 + nmr2
 elif escuacao == "Subtração":
  resultado = nmr1 - nmr2
 elif escuacao == "Divisão":
  if nmr2 == 0:
   resultado = " erro de divisao por zero"
  else:
   resultado = nmr1 / nmr2
 elif escuacao == "Multiplicação":
   resultado = nmr1 * nmr2

st.success(f"Resultado: {resultado}")
