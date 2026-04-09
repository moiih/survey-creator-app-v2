<!-- Button trigger modal -->
<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#staticBackdrop">
    Launch static backdrop modal
  </button>
  
  <!-- Modal -->
  <div class="modal fade" id="staticBackdrop" data-backdrop="static" data-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="staticBackdropLabel">How Would You Like To Call Your Q&A Form &quest;</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" onclick="redirect_from_title_modal()" data-dismiss="modal">Close</button>
          <input type="submit" class="btn btn-primary" value="Save Title">
        </div>
      </div>
    </div>
  </div>







  <form action="" method="POST" style="margin-top: 60px; margin-bottom: 60px; margin-left: 130px;">
             {% csrf_token %}
            <label for="title"> Quiz Title: </label>
            <input type="text" name="quiz_title" id="title" class="form-control col-7"/>

            <br>
            <input type="submit" class="btn btn-primary" value="Submit Title">
        </form>    










<div class="accordion" id="accordionExample">

  <div class="card">
    <div class="card-header" id="headingOne">
      <h2 class="mb-0">
        <button class="btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
          Collapsible Group Item #1
        </button>
      </h2>
    </div>

    <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordionExample">
      <div class="card-body">
        Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proident. Ad vegan excepteur butcher vice lomo. Leggings occaecat craft beer farm-to-table, raw denim aesthetic synth nesciunt you probably haven't heard of them accusamus labore sustainable VHS.
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header" id="headingTwo">
      <h2 class="mb-0">
        <button class="btn btn-link btn-block text-left collapsed" type="button" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
          Collapsible Group Item #2
        </button>
      </h2>
    </div>

    <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordionExample">
      <div class="card-body">
        Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proident. Ad vegan excepteur butcher vice lomo. Leggings occaecat craft beer farm-to-table, raw denim aesthetic synth nesciunt you probably haven't heard of them accusamus labore sustainable VHS.
      </div>
    </div>
  </div>

  <div class="card">
    <div class="card-header" id="headingThree">
      <h2 class="mb-0">
        <button class="btn btn-link btn-block text-left collapsed" type="button" data-toggle="collapse" data-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
          Collapsible Group Item #3
        </button>
      </h2>
    </div>

    <div id="collapseThree" class="collapse" aria-labelledby="headingThree" data-parent="#accordionExample">
      <div class="card-body">
        Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck quinoa nesciunt laborum eiusmod. Brunch 3 wolf moon tempor, sunt aliqua put a bird on it squid single-origin coffee nulla assumenda shoreditch et. Nihil anim keffiyeh helvetica, craft beer labore wes anderson cred nesciunt sapiente ea proident. Ad vegan excepteur butcher vice lomo. Leggings occaecat craft beer farm-to-table, raw denim aesthetic synth nesciunt you probably haven't heard of them accusamus labore sustainable VHS.
      </div>
    </div>
  </div>
  
</div>




































{% extends 'BASE.html' %}

{% block title %} Q&A Page {% endblock title %}

{% block quiz_content %}

<br><br>
<!-- <h1>Coming Soon...</h1> -->
    
    {% if show_quiz %}
        
        <div class="container col-4 offset-4">
            <div class="header panel-heading">
                <h2 style="width: 100; text-align: center; margin-left: 0px; margin-top: auto;"> Quiz Title : {{ title }} </h2>
            </div>
        <form action="" method="POST">
            {% for q in show_quiz %}
            <div class="content panel panel-default form-control" style="height: fit-content; box-shadow: 4px 5px 10px 1px rgb(0,0,0); border-radius: 12px;">            
                <div class="panel-body" style="text-align: center; height: min;">
                    
                    {% if q.image %}
                        <img src="{{ q.image.url }}" alt="Quiz Image" height="150" width="200" style="border: 2px solid black;"/> <br>
                    {% endif %}                                            

                    
                    {% if q.question %}
                        {{ q.question }}                        
                    {% endif %}         
                    
                    <hr class="my-4">
                                
                        {% if q.option_one %}                                                
                        <input type="radio" class="options_lefting" id="{{ q.option_one }}" name="{{ q.option_one }} + _second" value="option1"/> &nbsp;
                        <label for="{{ q.option_one }}" class="labels_lefting"> {{ q.option_one }} </label> <br>
                        {% endif %}                    

                        {% if q.option_two %}                        
                        <input type="radio" class="options_lefting" id="{{ q.option_two }}" name="{{ q.option_one }} + _second" value="option2"/> &nbsp;
                        <label for="{{ q.option_two }}" class="labels_lefting"> {{ q.option_two }} </label> <br>
                        {% endif %}                    
                        
                        {% if q.option_three %}
                            <input type="radio" class="options_lefting" id="{{ q.option_three }}" name="{{ q.option_one }} + _" value="option3"/>
                            <label for="{{ q.option_three }}" class="labels_lefting"> {{ q.option_three }} </label> <br>
                        {% endif %}                            

                        {% if q.option_four %}
                            <input type="radio" class="options_lefting" id="{{ q.option_four }}" name="{{ q.option_one }} + _" value="option4"/>
                            <label for="{{ q.option_four }}" class="labels_lefting"> {{ q.option_four }} </label> <br>
                        {% endif %}                            

                        {% if q.option_five %}
                            <input type="radio" class="options_lefting" id="{{ q.option_five }}" name="{{ q.option_one }} + _" value="option5"/>
                            <label for="{{ q.option_five }}" class="labels_lefting"> {{ q.option_five }} </label> <br>
                        {% endif %}                            

                        {% if q.option_six %}
                            <input type="radio" class="options_lefting" id="{{ q.option_six }}" name="{{ q.option_one }} + _" value="option6"/>
                            <label for="{{ q.option_six }}" class="labels_lefting"> {{ q.option_six }} </label> <br>
                        {% endif %}                                           

                </div>                
            </div>
            <br>
            {% endfor %}   
            
            <br>
            <input type="submit" class="btn btn-primary" style="margin-left: 210px;" value="Submit">

        </form>
        </div>                    
        <br> <br>
        
    {% endif %}    

{% endblock quiz_content %}











































{% extends 'BASE.html' %}

{% block title %} Create~Q&A {% endblock title %}

{% block quiz_content %}

<!-- <h1 style="margin-top: 200px; margin-left: 550px;">Heelllooooo !!!!!!!</h1> -->

<!-- Quiz Title is : {{ request.session.quiz_title }} -->

<br><br>
<center>
<div class="container col-8 offset-2.5">
    <div class="panel panel-default" style="box-shadow: 4px 5px 10px 1px rgb(0,0,0); border-radius: 12px; background-color: #000000; color: white; height: 1000px;">
        <div class="panel-heading">    

            <!-- For Messages(if any) -->
            {% if messages %}                    
                {% for message in messages %}
                    &boxdR;
                    <center><strong id="mg" style="color: #5cb85c; font-size: large; padding: 5px; background-color: white;">{{ message }}</strong></center>
                {% endfor %}                        
            {% endif %}        

            <h2 class="btn btn-primary col-md-12" style="font-size: 30px; cursor: none;" style="width: 100%;">                                 
                                    
                &bigstar; Create Your Q&A Form here &bigstar; <br>

                {% if request.session.page_count %}
                    <span style="float: left; font-size: 15px;"> Question Page: <span style="color: yellow;">{{ request.session.page_count }}</span> </span>

                    {% if request.session.quiz_title %}
                        <span style="float: right; font-size: 15px;"> Q&A Form Title is : <span style="color: yellow;">{{ request.session.quiz_title }}</span> </span>
                    {% endif %}

                {% else %}
                    
                    {% if total_questions %}
                        <span style="float: left; font-size: 15px;"> Total Questions: <span style="color: yellow;">{{ total_questions }}</span> </span>
                    {% endif %}

                    
                    {% if qtitle %}
                        <span style="float: right; font-size: 15px;"> Q&A Form Title is : <span style="color: yellow;">{{ qtitle }}</span> </span>
                    {% endif %}
                        
                                        
                {% endif %}

            </h2>
        </div>

        <div class="container highlight_field_create_quiz" style=" margin-top: 10px;">
            <br>
            <div style="float: left; width: 410px;">
            <form action="" method="POST" id="quiz_form" enctype="multipart/form-data" style="margin-left: 50px;">

                 {% csrf_token %}                
                <input type="hidden" name="quiz_title" value="{{ request.session.quiz_title }}">

                <input type="hidden" name="session_state" id="state">

                <label for="pic" style="margin-right: 212px;"> <strong><span class="circleNumber">1</span> Upload Image:</strong> </label>                
                <input type="file" name="image" id="pic" class="form-control col-12" style="border: none; background-color: #f0ad4e; color: white; margin-right: 30px; margin-left: 12px;"> <br><br>

                
                <label for="ques" style="margin-right: 200px;"> <strong><span class="circleNumber">2</span> Enter Question:</strong> </label>
                <textarea name="question" id="ques" rows="5" class="form-control col-12" style="border-radius: 9px; margin-left: 12px;"></textarea> <br>
                </div>
                



                <div style="float: right; border-left: 1px solid white; margin-right: 20px; padding-left: 40px;">
                <label for="opt1" aria-required="true"> <strong><span class="circleNumber">3</span> Select The Response Type:</strong> </label> <br>
                <div class="container" id="RadioChoice" style="margin-bottom: 15px;">
                    &nbsp;
                    <input type="radio" name="response_type" id="opt1" checked>
                    <label for="opt1"> Multiple Choice Typed </label>  &nbsp;
                    
                    <input type="radio" name="response_type" id="opt2">                
                    <label for="opt2"> Text Typed </label>
                </div>


                <div class="mcq container col-10 offset-1" id="opt1" style="border: 1px solid rgb(187, 183, 183); border-radius: 9px; margin-left: 40px; margin-top: 0;">
                    
                    <label for="fields_count_dropdown" style="margin-top: 35px;"> <span>Number Of Options You Want In This Question :</span> </label> 
                    <select name="" id="fields_count_dropdown" class="form-control col-10" onchange="show_fields()">                        
                        <option value="2"> <span>With Two Options Only</span> </option>
                        <option value="3" selected> <span>With Three Options Only</span> </option>
                        <option value="4"> <span>With Four Options Only</span> </option>
                        <option value="5"> <span>With Five Options Only</span> </option>
                        <option value="6"> <span>With Six Options Only</span> </option>
                    </select>

                    <label for="op1" style="margin-top: 20px; margin-right: 160px;" id="label1"> Option 1: </label><br>
                    <input type="text" name="option_one" id="op1" class="form-control col-9"><br>

                    <label for="op2" id="label2" style="margin-right: 160px;"> Option 2: </label><br>
                    <input type="text" name="option_two" id="op2" class="form-control col-9"><br>

                    <label for="op3"id="label3" style="margin-right: 160px;"> Option 3: </label><br>
                    <input type="text" name="option_three" id="op3" class="form-control col-9"><br>

                    <label for="op4" id="label4" style="margin-right: 160px;"> Option 4: </label><br>
                    <input type="text" name="option_four" id="op4" class="form-control col-9"><br>

                    <label for="op5" id="label5" style="margin-right: 160px;"> Option 5: </label><br>
                    <input type="text" name="option_five" id="op5" class="form-control col-9"><br>

                    <label for="op6" id="label6" style="margin-right: 160px;"> Option 6: </label><br>
                    <input type="text" name="option_six" id="op6" class="form-control col-9" style="margin-bottom: 10px;"><br>                    
                </div>
                </div>

                <br>
                <hr style="margin-top: 303px; margin-bottom: 12px; margin-left: 30px; border-color: white; width: 420px;">

                <br>
                <div class="myButtons" style="float:left; margin-right: 0px; margin-left: 105px;">
                    <button type="button" class="btn btn-primary btn-lg btn-outline-warning" style="border-radius: 50px; color: white; border: none;" onclick="add_new()"> <span style="font-size: 18px;">&plus;</span> <span>Add More</span> </button> &nbsp;
                    <input type="submit" class="btn btn-success btn-lg btn-outline-warning" value=" Finish " style="border-radius: 50px; color: white; border: none;">                                                        
                </div>                                                                                    

            </form>                        
            <br><br><br><br><br>

        </div>

    </div>
</div>
</center>

<br><br><br><br>



<script>    

   


    
/* To "Add(+) One More Question" Button */
    function change_session_state() {                
        document.getElementById("quiz_form").submit();        
    }



/* To "Add One More" */
    function add_new() {            
        console.log(document.getElementById("state").value);
        document.getElementById("state").value = "1";
        console.log(document.getElementById("state").value);
        //setTimeout(change_session_state, 3000);        
        document.getElementById("quiz_form").submit();                
    }



/* For "Response Type" Choice */
    $(document).ready(function(){

        $(".mcq").show();    

        $("#opt1").click(function(){
            $(".mcq").show();
        });

        $("#opt2").click(function(){
            $(".mcq").hide();
        });        
    });



/* For "Number Of Fields" Dropdown */
    var m;
    for(m=1; m<=6; m++) { 
        if( m<4 ) {
            $("#label"+m).show();
            $("#op"+m).show();
        }
        else {
            $("#label"+m).hide();
            $("#op"+m).hide();
        }
    }


    function show_fields() {
        var i;
        var temp;
        var x = document.getElementById("fields_count_dropdown").value;        
        x = Number(x);
        //console.log(x);
        
        for(i=1; i<=x; i++) {
            $("#label"+i).show();            
            $("#op"+i).show();
        }
        for(i=x+1; i<=6; i++) {
            $("#label"+i).hide();
            $("#op"+i).hide();
        }
    }
    
</script>


{% endblock quiz_content %}



















































{% extends 'BASE.html' %}

{% block title %} Create~Q&A {% endblock title %}

{% block quiz_content %}

<!-- <h1 style="margin-top: 200px; margin-left: 550px;">Heelllooooo !!!!!!!</h1> -->

<!-- Quiz Title is : {{ request.session.quiz_title }} -->

<br><br>
<center>
<div class="container col-8 offset-2.5">
    <div class="panel panel-default" style="box-shadow: 4px 5px 10px 1px rgb(0,0,0); border-radius: 12px; background-color: #000000; color: white; height: 1550px;">
        <div class="panel-heading">    

            <!-- For Messages(if any) -->
            {% if messages %}                    
                {% for message in messages %}
                    &boxdR;
                    <center><strong id="mg" style="color: #5cb85c; font-size: large; padding: 5px; background-color: white;">{{ message }}</strong></center>
                {% endfor %}                        
            {% endif %}        

            <h2 class="btn btn-primary col-md-12" style="font-size: 30px; cursor: none;" style="width: 100%;">                                 
                                    
                &bigstar; Create Your Q&A Form here &bigstar; <br>

                {% if request.session.page_count %}
                    <span style="float: left; font-size: 15px;"> Question Page: <span style="color: yellow;">{{ request.session.page_count }}</span> </span>

                    {% if request.session.quiz_title %}
                        <span style="float: right; font-size: 15px;"> Q&A Form Title is : <span style="color: yellow;">{{ request.session.quiz_title }}</span> </span>
                    {% endif %}

                {% else %}
                    
                    {% if total_questions %}
                        <span style="float: left; font-size: 15px;"> Total Questions: <span style="color: yellow;">{{ total_questions }}</span> </span>
                    {% endif %}

                    
                    {% if qtitle %}
                        <span style="float: right; font-size: 15px;"> Q&A Form Title is : <span style="color: yellow;">{{ qtitle }}</span> </span>
                    {% endif %}
                        
                                        
                {% endif %}

            </h2>
        </div>

        <div class="container highlight_field_create_quiz" style=" margin-top: 10px;">
            <br>
            <div style="float: left; width: 410px;">
            <form action="" method="POST" id="quiz_form" enctype="multipart/form-data" style="margin-left: 50px;">

                 {% csrf_token %}                
                <input type="hidden" name="quiz_title" value="{{ request.session.quiz_title }}">

                <input type="hidden" name="session_state" id="state">

                <label for="pic" style="margin-right: 212px;"> <strong><span class="circleNumber">1</span> Upload Image:</strong> </label>                
                <input type="file" name="image" id="pic" class="form-control col-12" style="border: none; background-color: #f0ad4e; color: white; margin-right: 30px; margin-left: 12px;"> <br><br>

                
                <label for="ques" style="margin-right: 200px;"> <strong><span class="circleNumber">2</span> Enter Question:</strong> </label>
                <textarea name="question" id="ques" rows="5" class="form-control col-12" style="border-radius: 9px; margin-left: 12px;"></textarea> <br>
                </div>
                



                <div style="float: right; border-left: 1px solid white; margin-right: 20px; padding-left: 40px;">
                <label for="opt1" aria-required="true"> <strong><span class="circleNumber">3</span> Select The Response Type:</strong> </label> <br>
                <div class="container" id="RadioChoice" style="margin-bottom: 15px;">
                    &nbsp;
                    <input type="radio" name="response_type" id="opt1" checked>
                    <label for="opt1"> Multiple Choice Typed </label>  &nbsp;
                    
                    <input type="radio" name="response_type" id="opt2">                
                    <label for="opt2"> Text Typed </label>
                </div>


                <div class="mcq container col-10 offset-1" id="opt1" style="border: 1px solid rgb(187, 183, 183); border-radius: 9px; margin-left: 40px; margin-top: 0;">
                    
                    <label for="fields_count_dropdown" style="margin-top: 35px;"> <span>Number Of Options You Want In This Question :</span> </label> 
                    <select name="" id="fields_count_dropdown" class="form-control col-10" onchange="show_fields()">                        
                        <option value="2"> <span>With Two Options Only</span> </option>
                        <option value="3" selected> <span>With Three Options Only</span> </option>
                        <option value="4"> <span>With Four Options Only</span> </option>
                        <option value="5"> <span>With Five Options Only</span> </option>
                        <option value="6"> <span>With Six Options Only</span> </option>
                    </select>

                    <label for="op1" style="margin-top: 20px; margin-right: 160px;" id="label1"> Option 1: </label><br>
                    <input type="text" name="option_one" id="op1" class="form-control col-9"><br> 
                    <label for="correct_1" style="margin-right: 80px;" id="clabel_1"> Correct Option 1: </label><br>
                    <input type="text" name="correct_1" id="correct_1" class="form-control col-9" style="margin-left: 20px;"><br>                    

                    <label for="op2" id="label2" style="margin-right: 160px;"> Option 2: </label><br>
                    <input type="text" name="option_two" id="op2" class="form-control col-9"><br>
                               

                    <label for="op3" id="label3" style="margin-right: 160px;"> Option 3: </label><br>
                    <input type="text" name="option_three" id="op3" class="form-control col-9"><br>                    

                    <label for="op4" id="label4" style="margin-right: 160px;"> Option 4: </label><br>
                    <input type="text" name="option_four" id="op4" class="form-control col-9"><br>                    

                    <label for="op5" id="label5" style="margin-right: 160px;"> Option 5: </label><br>
                    <input type="text" name="option_five" id="op5" class="form-control col-9"><br>                    

                    <label for="op6" id="label6" style="margin-right: 160px;"> Option 6: </label><br>
                    <input type="text" name="option_six" id="op6" class="form-control col-9"><br>                       
                </div>
                </div>

                <br>
                <hr style="margin-top: 303px; margin-bottom: 12px; margin-left: 30px; border-color: white; width: 420px;">

                <br>
                <div class="myButtons" style="float:left; margin-right: 0px; margin-left: 105px;">
                    <button type="button" class="btn btn-primary btn-lg btn-outline-warning" style="border-radius: 50px; color: white; border: none;" onclick="add_new()"> <span style="font-size: 18px;">&plus;</span> <span>Add More</span> </button> &nbsp;
                    <input type="submit" class="btn btn-success btn-lg btn-outline-warning" value=" Finish " style="border-radius: 50px; color: white; border: none;">                                                        
                </div>                                                                                    

            </form>                        
            <br><br><br><br><br>

        </div>

    </div>
</div>
</center>

<br><br><br><br>



<script>    

   


    
/* To "Add(+) One More Question" Button */
    function change_session_state() {                
        document.getElementById("quiz_form").submit();        
    }



/* To "Add One More" */
    function add_new() {            
        console.log(document.getElementById("state").value);
        document.getElementById("state").value = "1";
        console.log(document.getElementById("state").value);
        //setTimeout(change_session_state, 3000);        
        document.getElementById("quiz_form").submit();                
    }



/* For "Response Type" Choice */
    $(document).ready(function(){

        $(".mcq").show();    

        $("#opt1").click(function(){
            $(".mcq").show();
        });

        $("#opt2").click(function(){
            $(".mcq").hide();
        });        
    });



/* For "Number Of Fields" Dropdown */
    var m;
    for(m=1; m<=6; m++) { 
        if( m<4 ) {
            $("#label"+m).show();
            $("#op"+m).show();            
        }
        else {
            $("#label"+m).hide();
            $("#op"+m).hide();            
        }
    }


    function show_fields() {
        var i;
        var temp;
        var x = document.getElementById("fields_count_dropdown").value;        
        x = Number(x);
        //console.log(x);
        
        for(i=1; i<=x; i++) {
            $("#label"+i).show();            
            $("#op"+i).show();            
        }
        for(i=x+1; i<=6; i++) {
            $("#label"+i).hide();
            $("#op"+i).hide();            
        }
    }
    
</script>


{% endblock quiz_content %}