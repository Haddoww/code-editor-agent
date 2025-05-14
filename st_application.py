import streamlit as st
from file_handler import save_uploaded_file, read_file
from agent import enhance_code, generate_user_goal, generate_plan, generate_plan_and_prepare, run_tool_on_code
from tools import pause_and_reassess, create_new_doc


st.set_page_config(page_title="Code Assistant Agent")
st.title("🧠 Context-Aware Code Assistant")



#init chat history
#if "messages" not in st.session_state:
#    st.session_state.messages = []

#accept user input
#if prompt:= st.chat_input("Lets look at what you vibe coded"):
#    #display that input
##    with st.chat_message("user"):
 #       st.markdown(prompt)
 #   st.session_state.messages.append({"role": "user", "content": prompt})





uploaded_file = st.file_uploader("Upload your code file", type=["py"])

if uploaded_file:
    file_path = save_uploaded_file(uploaded_file)
    original_code = read_file(file_path)
    st.subheader("Original Code")
    st.code(original_code, language="python")

    user_goal  = st.text_input("What would you like the assistant to do with this code")
    if user_goal and st.button("Enhance with Agent"):
        
        plan, current_code, txt = generate_plan_and_prepare(original_code ,user_goal)
        st.markdown(txt)


        #enhanced_code, enhanced_code_log, plan = enhance_code(original_code, user_goal)
        #st.subheader("Enhanced Code")
        #st.code(enhanced_code, language="python")

        #st.subheader("Reasoned Plan")
        #st.markdown(plan)

        for step in plan:

            if step == "pause":
                st.markdown("paused")
                reassessment = pause_and_reassess(current_code, original_code, user_goal, plan[plan.index(step) + 1:]) 
                if reassessment == "STOP":
                    break
                else: 
                    plan = plan[:plan.index(step) + 1] + reassessment
                continue
            st.markdown(f"### 🔧 Step: `{step}`")
            current_code = run_tool_on_code(step, current_code)
            #tool = TOOLS[step]
            st.code(current_code, language="python")

        st.markdown("Done")

